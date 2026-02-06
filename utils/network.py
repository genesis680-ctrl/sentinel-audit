import requests
import os

class NetworkManager:
    @staticmethod
    def download_file(url, destination):
        """Baixa um documento publico para processamento local."""
        try:
            print(f"[*] Baixando alvo: {url}")
            response = requests.get(url, timeout=15, stream=True)
            response.raise_for_status()

            with open(destination, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            return True
        except Exception as e:
            print(f"[!] Erro no download: {e}")
            return False

    @staticmethod
    def cleanup(file_path):
        """Remove o arquivo temporario apos a auditoria (Seguranca de Dados)."""
        if os.path.exists(file_path):
            os.remove(file_path)
