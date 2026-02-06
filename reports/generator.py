import os
from datetime import datetime

class ReportGenerator:
    def __init__(self, output_dir="reports"):
        self.output_dir = output_dir
        # Garante que a pasta existe
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def generate(self, findings, source_name="Auditoria_Manual"):
        """
        Gera um relatório Markdown profissional baseado nos achados.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"Relatorio_Sentinela_{timestamp}.md"
        filepath = os.path.join(self.output_dir, filename)

        # 1. Estatísticas
        total_findings = len(findings)
        by_type = {}
        for f in findings:
            tipo = f.get('tipo', 'DESCONHECIDO')
            by_type[tipo] = by_type.get(tipo, 0) + 1

        # 2. Construção do Conteúdo Markdown
        md_content = f"""# 🛡️ Relatório de Auditoria Sentinela

**Data de Geração:** {datetime.now().strftime("%d/%m/%Y às %H:%M")}
**Fonte Auditada:** `{source_name}`
**Status:** {"🔴 CRÍTICO" if total_findings > 0 else "🟢 SEGURO"}

---

## 📊 Resumo Executivo
O sistema **Auditoria Sentinela** realizou uma varredura automatizada em busca de Dados Pessoais Sensíveis (PII) em conformidade com a LGPD.

* **Total de Vulnerabilidades:** {total_findings}
* **Tipos Detectados:**
"""
        
        for tipo, count in by_type.items():
            md_content += f"    * **{tipo}:** {count} ocorrências\n"

        if total_findings == 0:
            md_content += "\n✅ **Nenhuma não-conformidade foi detectada nesta amostra.**\n"
        else:
            md_content += f"""
---

## 🔍 Detalhamento Técnico
Abaixo estão listados os registros anonimizados para validação.

| Tipo | Dado Mascarado | Hash de Verificação (SHA-256) |
| :--- | :--- | :--- |
"""
            for f in findings:
                md_content += f"| {f['tipo']} | `{f['masked']}` | `{f['hash'][:16]}...` |\n"

            md_content += """
---

## ⚠️ Recomendações de Segurança
1.  **Remoção Imediata:** Os documentos listados acima contêm dados expostos e devem ser retirados de circulação pública imediatamente.
2.  **Revisão de Processos:** Verificar o fluxo de publicação que permitiu a exposição desses dados.
3.  **Notificação:** Avaliar a necessidade de notificar os titulares conforme Art. 48 da LGPD.

---
*Gerado automaticamente pelo framework Auditoria Sentinela v1.0*
"""

        # 3. Salvar Arquivo
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)
            
        return filepath
