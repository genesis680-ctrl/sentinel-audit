import os
from pypdf import PdfReader

def extract_text(file_path):
    """
    Extrai texto limpo de arquivos, diferenciando PDF de texto comum.
    """
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == '.pdf':
        print(f"📄 Processando PDF: {os.path.basename(file_path)}...")
        try:
            reader = PdfReader(file_path)
            full_text = []
            
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    full_text.append(text)
            
            return "\n".join(full_text)
            
        except Exception as e:
            print(f"⚠️ Erro ao ler PDF (pode estar criptografado ou corrompido): {e}")
            return ""
    
    else:
        # Comportamento original para .txt, .html, etc.
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        except Exception as e:
            print(f"⚠️ Erro ao ler arquivo de texto: {e}")
            return ""
