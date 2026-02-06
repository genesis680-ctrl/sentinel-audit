import sys
import os
from engine.processor import DocumentProcessor
from reports.generator import ReportGenerator

def main():
    # 1. Verificação de Entrada
    if len(sys.argv) < 2:
        print("❌ Uso correto: python main.py [ARQUIVO_PARA_AUDITAR]")
        print("Exemplo: python main.py leak_test.txt")
        return

    target_file = sys.argv[1]

    # 2. Validação se o arquivo existe
    if not os.path.exists(target_file):
        print(f"❌ Erro: O arquivo '{target_file}' não foi encontrado.")
        return

    print(f"🔄 Iniciando auditoria em: {target_file}...")

    # 3. Processamento (Busca e Validação)
    try:
        processor = DocumentProcessor('rules/patterns.json')
        findings = processor.scan_file(target_file)
        print(f"✅ Processamento concluído. Vulnerabilidades encontradas: {len(findings)}")
    except Exception as e:
        print(f"❌ Erro crítico no motor: {str(e)}")
        return

    # 4. Geração de Relatório
    try:
        generator = ReportGenerator()
        report_path = generator.generate(findings, source_name=target_file)
        print(f"\n📄 Relatório disponível em:\n   👉 {report_path}")
    except Exception as e:
        print(f"❌ Erro ao gerar relatório: {str(e)}")

if __name__ == "__main__":
    main()
