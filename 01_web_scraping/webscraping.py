import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

# Diretórios e Nomes
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
DIR_DOWNLOADS = r"C:\INTUITIVE\01_web_scraping\downloads"
ZIP_NAME = os.path.join(DIR_DOWNLOADS, "anexos.zip")


def baixar_pdf(url, nome_arquivo):
    """Baixa um PDF e verifica se está íntegro."""
    resposta = requests.get(url, stream=True)
    if resposta.status_code == 200:
        caminho_arquivo = os.path.join(DIR_DOWNLOADS, nome_arquivo)
        with open(caminho_arquivo, 'wb') as f:
            f.write(resposta.content)
        # Verifica se o PDF não está corrompido (tamanho > 10 KB)
        if os.path.getsize(caminho_arquivo) > 10 * 1024:
            print(f"Download OK: {nome_arquivo}")
            return True
        else:
            os.remove(caminho_arquivo)  # Remove arquivo corrompido
            print(f"Arquivo corrompido: {nome_arquivo}")
    return False

def extrair_links_pdf():
    # Extraindo links da pagina html 
    resposta = requests.get(URL)
    soup = BeautifulSoup(resposta.text, 'html.parser')
    
    anexos = []
    for link in soup.find_all('a', href=True):
        texto_link = link.text.strip().lower()
        href = link['href'].lower()
        # Filtra apenas PDFs com "Anexo I" ou "Anexo II" no texto E no link
        if ("anexo i" in texto_link or "anexo ii" in texto_link) and href.endswith('.pdf'):
            anexos.append(link['href'])
    return anexos[:2]  

def compactar_anexos():
    # Compactando os Anexos
    with ZipFile(ZIP_NAME, 'w') as zipf:
        for arquivo in os.listdir(DIR_DOWNLOADS):
            if arquivo.endswith('.pdf'):
                caminho = os.path.join(DIR_DOWNLOADS, arquivo)
                zipf.write(caminho, arquivo)
    print(f"Compactado em: {ZIP_NAME}")

def main():
    
    # Extração 
    links_pdf = extrair_links_pdf()
    
    # Download
    for i, url in enumerate(links_pdf, start=1):
        nome_arquivo = f"Anexo_{i}.pdf"
        baixar_pdf(url, nome_arquivo)
    
    # Compactando 
    compactar_anexos()

if __name__ == "__main__":
    main()