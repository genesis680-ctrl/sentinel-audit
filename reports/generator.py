from datetime import datetime

class ReportGenerator:
    def __init__(self, target_name):
        self.target_name = target_name
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def generate_markdown(self, findings):
        """Cria um relatorio tecnico em formato Markdown."""
        report_lines = [
            f"# RELATÓRIO TÉCNICO DE AUDITORIA DE DADOS",
            f"**Alvo:** {self.target_name}",
            f"**Data da Varredura:** {self.timestamp}",
            f"**Status:** Alerta de Violação de LGPD",
            "\n---",
            "\n## 1. Sumário Executivo",
            f"Durante a execução da auditoria automatizada, foram identificadas {len(findings)} ocorrências de dados sensíveis expostos em conformidade com os padrões da Lei Geral de Proteção de Dados (LGPD).",
            "\n## 2. Detalhes das Ocorrências",
            "| Tipo | Dado Mascarado | Impressão Digital (SHA-256) |",
            "| :--- | :--- | :--- |"
        ]

        for item in findings:
            report_lines.append(f"| {item['type']} | {item['masked']} | `{item['fingerprint'][:32]}...` |")

        report_lines.extend([
            "\n## 3. Recomendações Técnicas",
            "1. **Remediação Imediata:** Remover ou anonimizar os dados identificados no arquivo fonte.",
            "2. **Revisão de Governança:** Avaliar o processo de publicação de documentos para implementar filtros preventivos.",
            "3. **Auditoria de Log:** Verificar quem acessou este documento desde a sua publicação.",
            "\n---",
            "\n*Este relatório foi gerado automaticamente pelo Sentinel Audit Framework.*"
        ])

        return "\n".join(report_lines)

    def save_report(self, content, filename="RELATORIO_AUDITORIA.md"):
        """Salva o conteudo em um arquivo na pasta de relatorios."""
        path = f"reports/{filename}"
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path
