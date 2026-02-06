import re
import json
import os
from pypdf import PdfReader
from engine.auditor import process_match

class DocumentProcessor:
    def __init__(self, rules_path):
        self.rules = self._load_rules(rules_path)

    def _load_rules(self, path):
        with open(path, 'r') as f:
            return json.load(f)

    def _extract_text_from_pdf(self, file_path):
        """Extrai texto de todas as paginas de um PDF."""
        text = ""
        try:
            reader = PdfReader(file_path)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        except Exception as e:
            print(f"[!] Erro ao ler PDF: {e}")
        return text

    def scan_file(self, file_path):
        findings = []
        if not os.path.exists(file_path):
            return {"error": "Arquivo nao encontrado"}

        # Decisao de motor de leitura baseada na extensao
        if file_path.lower().endswith('.pdf'):
            content = self._extract_text_from_pdf(file_path)
        else:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
        for label, rule_data in self.rules.items():
            pattern = rule_data['regex']
            matches = re.findall(pattern, content)
            for m in matches:
                result = process_match(m, label)
                if result['valid']:
                    findings.append({
                        "type": label.upper(),
                        "masked": result['masked'],
                        "fingerprint": result['hash']
                    })
        return findings
