import sys
from engine.processor import DocumentProcessor
from reports.generator import ReportGenerator
from utils.network import NetworkManager
from utils.extractor import LinkExtractor

def audit_target(target, processor):
    """Funcao auxiliar para auditar um unico alvo (local ou URL)."""
    TEMP_FILE = 'tmp_audit_target.pdf' if target.endswith('.pdf') else 'tmp_audit_target.txt'
    
    if target.startswith("http"):
        if not NetworkManager.download_file(target, TEMP_FILE):
            return None
        target_name = target
    else:
        TEMP_FILE = target
        target_name = target

    results = processor.scan_file(TEMP_FILE)
    
    if target.startswith("http") and target != 'leak_test.txt':
        NetworkManager.cleanup(TEMP_FILE)
        
    return results, target_name

def run_suite(initial_target):
    print(f"--- SENTINEL AUDIT: MODO HUNTER ATIVADO ---")
    processor = DocumentProcessor('rules/patterns.json')
    all_findings = []

    # Se o alvo for um site (sem ser PDF direto), extrai os links primeiro
    if initial_target.startswith("http") and not initial_target.lower().endswith(".pdf"):
        links = LinkExtractor.get_pdf_links(initial_target)
        print(f"[+] Encontrados {len(links)} PDFs para auditoria.")
        
        for link in links:
            res, name = audit_target(link, processor)
            if res:
                for r in res:
                    r['source'] = name
                    all_findings.append(r)
    else:
        # Auditoria de alvo unico (Arquivo ou PDF direto)
        res, name = audit_target(initial_target, processor)
        if res:
            for r in res:
                r['source'] = name
                all_findings.append(r)

    # Geracao de Relatorio Consolidado
    if not all_findings:
        print("[-] Nenhum vazamento detectado na varredura.")
    else:
        print(f"[!] ALERTA: {len(all_findings)} vulnerabilidades encontradas no total!")
        reporter = ReportGenerator(target_name=initial_target)
        report_path = reporter.save_report(reporter.generate_markdown(all_findings))
        print(f"[+] SUCESSO: Relatorio consolidado em: {report_path}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else 'leak_test.txt'
    run_suite(target)
