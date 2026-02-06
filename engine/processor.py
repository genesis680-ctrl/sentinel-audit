import re
import json
from engine.auditor import process_match

class DocumentProcessor:
    def __init__(self, rules_path):
        with open(rules_path, 'r') as f:
            self.rules = json.load(f)

    def scan_file(self, file_path):
        findings = []
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Itera sobre as regras definidas no patterns.json
        for label, rule_data in self.rules.items():
            pattern = rule_data['regex']
            matches = re.findall(pattern, content)
            
            for m in matches:
                # Agora passamos o dado e o label (ex: "cpf")
                result = process_match(m, label)
                if result.get('valid'):
                    findings.append({
                        "tipo": label.upper(),
                        "masked": result.get('masked'),
                        "hash": result.get('hash')
                    })
        return findings
