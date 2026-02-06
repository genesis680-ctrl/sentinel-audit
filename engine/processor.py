import re
import json
from engine.auditor import process_match
from utils.extractor import extract_text

class DocumentProcessor:
    def __init__(self, rules_path):
        with open(rules_path, 'r') as f:
            self.rules = json.load(f)

    def scan_file(self, file_path):
        findings = []
        
        # 1. Extração Inteligente (Aqui está a mágica da V2.0)
        content = extract_text(file_path)

        if not content:
            return []

        # 2. Varredura com Regex
        for label, rule_data in self.rules.items():
            pattern = rule_data['regex']
            
            # Regex multiline ajuda em textos extraídos de PDF
            matches = re.findall(pattern, content, re.MULTILINE)
            
            for m in matches:
                result = process_match(m, label)
                if result.get('valid'):
                    findings.append({
                        "tipo": label.upper(),
                        "masked": result.get('masked'),
                        "hash": result.get('hash')
                    })
        return findings
