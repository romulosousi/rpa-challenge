import requests
def download_excel(url: str, filename="challenge.xlsx"):
    try:
        r = requests.get(url)
        with open(filename, "wb") as f:
            f.write(r.content)
        
        print(f"Arquivo salvo com sucesso como '{filename}'")
        return filename
    except requests.exceptions.RequestException as e:
        print(f"ERRO ao baixar o arquivo: {e}")
        return None