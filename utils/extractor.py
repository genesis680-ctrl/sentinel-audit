import re
import requests
from urllib.parse import urljoin

class LinkExtractor:
    @staticmethod
    def get_pdf_links(target_url):
        """Varre uma pagina HTML em busca de links para arquivos PDF."""
        print(f"[*] Escaneando pagina em busca de PDFs: {target_url}")
        pdf_links = []
        try:
            response = requests.get(target_url, timeout=15)
            response.raise_for_status()
            
            # Regex para encontrar links que terminam em .pdf
            links = re.findall(r'href=["\'](.*?\.pdf)["\']', response.text, re.IGNORECASE)
            
            for link in links:
                # Converte links relativos em URLs completas
                full_url = urljoin(target_url, link)
                pdf_links.append(full_url)
                
            return list(set(pdf_links)) # Remove duplicados
        except Exception as e:
            print(f"[!] Erro ao extrair links: {e}")
            return []
