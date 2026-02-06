import os
import markdown
from datetime import datetime

class ReportGenerator:
    def __init__(self, output_dir="reports"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def generate(self, findings, source_name="Auditoria_Manual"):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        date_display = datetime.now().strftime("%d/%m/%Y às %H:%M")
        
        # Estatísticas
        total = len(findings)
        status_color = "#dc3545" if total > 0 else "#28a745" # Vermelho ou Verde
        status_text = "CRÍTICO - VAZAMENTO DETECTADO" if total > 0 else "SEGURO - NENHUMA EXPOSIÇÃO"

        # 1. Conteúdo Markdown (Mantemos o original para registro)
        md_content = f"""# 🛡️ Relatório de Auditoria Sentinela
**Data:** {date_display}
**Alvo:** `{source_name}`
**Status:** {status_text}

---
## 📊 Resumo Executivo
Auditoria automatizada de conformidade LGPD.
* **Vulnerabilidades:** {total}
* **Ação Recomendada:** Remoção imediata e notificação.

## 🔍 Evidências (Amostra Anonimizada)
| Tipo | Dado Mascarado | Hash SHA-256 |
| :--- | :--- | :--- |
"""
        for f in findings:
            md_content += f"| {f['tipo']} | `{f['masked']}` | `{f['hash'][:10]}...` |\n"

        md_content += "\n*Gerado por Auditoria Sentinela v2.0*"

        # Salva MD
        md_filename = f"Relatorio_Sentinela_{timestamp}.md"
        md_path = os.path.join(self.output_dir, md_filename)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        # 2. Conteúdo HTML (O "Bonitão" para PDF)
        # CSS Embutido para parecer documento oficial
        css_style = """
        <style>
            body { font-family: 'Helvetica', 'Arial', sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }
            .header { border-bottom: 2px solid #333; padding-bottom: 10px; margin-bottom: 30px; }
            .logo { font-size: 24px; font-weight: bold; color: #2c3e50; }
            .meta { font-size: 14px; color: #666; margin-top: 5px; }
            .alert { padding: 15px; background-color: """ + status_color + """; color: white; font-weight: bold; border-radius: 5px; text-align: center; margin: 20px 0; }
            table { width: 100%; border-collapse: collapse; margin: 20px 0; }
            th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
            th { background-color: #f2f2f2; color: #333; }
            tr:nth-child(even) { background-color: #f9f9f9; }
            code { background-color: #eee; padding: 2px 5px; border-radius: 3px; font-family: monospace; }
            .footer { margin-top: 50px; font-size: 12px; text-align: center; color: #999; border-top: 1px solid #eee; padding-top: 20px; }
        </style>
        """

        html_rows = ""
        for f in findings:
            html_rows += f"<tr><td>{f['tipo']}</td><td><code>{f['masked']}</code></td><td><code>{f['hash']}</code></td></tr>"

        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head><meta charset="UTF-8">{css_style}</head>
        <body>
            <div class="header">
                <div class="logo">🛡️ Auditoria Sentinela</div>
                <div class="meta">Relatório Técnico de Conformidade LGPD</div>
            </div>

            <div class="alert">{status_text}</div>

            <p><strong>Data da Análise:</strong> {date_display}</p>
            <p><strong>Fonte Auditada:</strong> {source_name}</p>

            <h2>1. Resumo Executivo</h2>
            <p>O sistema realizou uma varredura automatizada e identificou <strong>{total}</strong> registros de dados pessoais expostos publicamente. A exposição destes dados infringe princípios de minimização de dados da legislação vigente.</p>

            <h2>2. Detalhamento Técnico</h2>
            <p>Abaixo estão listadas as evidências encontradas. Os dados foram anonimizados (mascarados) para proteção neste relatório.</p>
            
            <table>
                <thead><tr><th>Tipo</th><th>Dado Exposto</th><th>Hash de Validação</th></tr></thead>
                <tbody>{html_rows}</tbody>
            </table>

            <h2>3. Recomendações</h2>
            <ul>
                <li><strong>Imediato:</strong> Remover o documento público ou aplicar tarja preta (redação) sobre os dados.</li>
                <li><strong>Processo:</strong> Rever fluxo de publicação no Diário Oficial.</li>
            </ul>

            <div class="footer">
                Relatório gerado automaticamente por Auditoria Sentinela Framework.<br>
                Este documento é confidencial e destinado aos responsáveis pelo tratamento de dados.
            </div>
        </body>
        </html>
        """

        html_filename = f"Relatorio_Sentinela_{timestamp}.html"
        html_path = os.path.join(self.output_dir, html_filename)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        return html_path  # Retorna o HTML que é o foco agora
