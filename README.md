# Auditoria Sentinela 🛡️

**Auditoria Sentinela** é um framework de auditoria automatizada para detecção de vazamentos de dados sensíveis (PII) em conformidade com a **LGPD (Lei Geral de Proteção de Dados)**. Desenvolvido para rodar 100% em ambiente mobile via **Termux**, o sistema foca na transparência pública e segurança da informação.

## 🚀 Funcionalidades
- **Validação Matemática:** Algoritmo de verificação de CPFs reais via módulo 11, eliminando falsos positivos.
- **Privacy by Design:** Anonimização de dados sensíveis via Hashing (SHA-256) nos registros de auditoria.
- **Leitura de PDFs:** Extração e análise de texto em documentos oficiais e editais complexos.
- **Modo Hunter:** Crawler integrado para extração automática de links de PDF em portais de transparência.
- **Relatórios Técnicos:** Geração automática de relatórios em Markdown para DPOs e gestores.
- **Automação:** Agendamento de varreduras diárias via Cron.

## 🛠️ Tecnologias
- **Python 3.12+**
- **PyPDF** (Processamento de PDFs)
- **Requests** (Comunicação de rede)
- **Git/GitHub** (Versionamento e Deploy)

## 📐 Lógica de Validação (CPF)
O sistema utiliza o cálculo dos dígitos verificadores para confirmar a autenticidade do documento:
$$D_1 = \left( \sum_{i=0}^{8} \text{CPF}_i \times (10 - i) \right) \times 10 \pmod{11}$$
$$D_2 = \left( \sum_{i=0}^{9} \text{CPF}_i \times (11 - i) \right) \times 10 \pmod{11}$$

## 📂 Estrutura do Projeto
- **`motor/`**: Núcleo de processamento e lógica de auditoria.
- **`regras/`**: Padrões de busca (RegEx) para CPFs, e-mails e chaves PIX.
- **`relatórios/`**: Repositório de resultados e documentos gerados.
- **`utilitários/`**: Módulos de rede, extração de links e notificações.
- **`setup.sh`**: Script de instalação automatizada das dependências.

## 📥 Instalação e Uso
Para configurar o ambiente no Termux, utilize o instalador automático:
```bash
bash setup.sh
python main.py [URL_DO_SITE_OU_ARQUIVO]
Projeto desenvolvido por Andre para fins de demonstração técnica em Segurança da Informação e Governança.
