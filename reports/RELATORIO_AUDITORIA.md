# RELATÓRIO TÉCNICO DE AUDITORIA DE DADOS
**Alvo:** leak_test.txt
**Data da Varredura:** 2026-02-05 23:06:02
**Status:** Alerta de Violação de LGPD

---

## 1. Sumário Executivo
Durante a execução da auditoria automatizada, foram identificadas 2 ocorrências de dados sensíveis expostos em conformidade com os padrões da Lei Geral de Proteção de Dados (LGPD).

## 2. Detalhes das Ocorrências
| Tipo | Dado Mascarado | Impressão Digital (SHA-256) |
| :--- | :--- | :--- |
| CPF | ***.982.***-25 | `7281dfb5e8becca0a1c5e77c1268baac...` |
| EMAIL | a***@gmail.com | `3275f79f28aca860b486fae987aab221...` |

## 3. Recomendações Técnicas
1. **Remediação Imediata:** Remover ou anonimizar os dados identificados no arquivo fonte.
2. **Revisão de Governança:** Avaliar o processo de publicação de documentos para implementar filtros preventivos.
3. **Auditoria de Log:** Verificar quem acessou este documento desde a sua publicação.

---

*Este relatório foi gerado automaticamente pelo Sentinel Audit Framework.*