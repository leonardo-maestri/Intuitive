
import pandas as pd
from tabula import read_pdf
from zipfile import ZipFile
import os

# Diretórios e Nomes
caminho_pdf = r"C:\INTUITIVE\01_web_scraping\downloads\Anexo_1.pdf"
pasta_saida = r"C:\INTUITIVE\02_transformacao_dados"
nome_csv = "Rol_de_Procedimentos.csv"
nome_zip = "LeonardoMaestriCintra.zip"

# Dicionário para traduzir as abreviações
traducao_colunas = {
    'OD': 'Seg. Odontológica',
    'AMB': 'Seg. Ambulatória'
}

# Lista completa das colunas na ordem correta
colunas_completas = [
    'PROCEDIMENTO', 'RN', 'VIGÊNCIA', 'Seg. Odontológica', 'Seg. Ambulatória',
    'HCO', 'HSO', 'REF', 'PAC', 'DUT', 'SUBGRUPO', 'GRUPO', 'CAPÍTULO'
]

def extrair_dados_pdf():

    print("Iniciando extração dos dados do PDF...")
    
    try:
        # Lendo todas as páginas do PDF
        tabelas = read_pdf(
            caminho_pdf,
            pages='all',
            multiple_tables=True,
            lattice=True,
            stream=True,
            pandas_options={'header': None},
            guess=False
        )
        
        if not tabelas:
            raise Exception("Não foi possível encontrar tabelas no PDF")
        
        # Juntando as tabelas
        dados_completos = pd.concat(tabelas, ignore_index=True)
        
        # Removendo linhas completamente vazias
        dados_completos = dados_completos.dropna(how='all')
        
        return dados_completos
    
    except Exception as e:
        print(f"Erro durante a extração: {str(e)}")
        raise

def ajustar_nomes_colunas(cabecalhos):
    #Padronizando os nomes das colunas e Tratando coluna RN
    nomes_ajustados = []
    for nome in cabecalhos:
        nome = str(nome).strip()
        # Corrigindo o nome da coluna RN (alteração)
        if "RN" in nome and "alteração" in nome:
            nomes_ajustados.append("RN")
        else:
            nomes_ajustados.append(nome)
    return nomes_ajustados

def identificar_cabecalho(linha, colunas_esperadas):
    # verifica se a linha é um cabeçalho
    valores = [str(x).strip() for x in linha]
    # Conta quantos valores batem com os nomes esperados
    correspondencias = sum(1 for valor in valores if valor in colunas_esperadas)
    return correspondencias >= 5

def processar_dados(dados_brutos):
    
    print("Processando dados extraídos...")
    
    # Procurando pelo cabeçalho nas primeiras linhas
    linha_cabecalho = None
    for i in range(min(10, len(dados_brutos))):
        if identificar_cabecalho(dados_brutos.iloc[i], colunas_completas + list(traducao_colunas.keys())):
            linha_cabecalho = i
            break
    
    if linha_cabecalho is None:
        raise Exception("Não foi possível identificar o cabeçalho na tabela")
    
    # Separando cabeçalhos e dados
    cabecalhos = ajustar_nomes_colunas(dados_brutos.iloc[linha_cabecalho])
    dados = dados_brutos.iloc[linha_cabecalho+1:].reset_index(drop=True)
    
    # Removendo repetições do cabeçalho
    dados = dados[~dados.apply(
        lambda linha: identificar_cabecalho(linha, colunas_completas + list(traducao_colunas.keys())), 
        axis=1
    )]
    
    # Criando o DataFrame final
    df_final = pd.DataFrame()
    
    # Mapeando as colunas encontradas para o formato desejado
    for indice, nome_coluna in enumerate(cabecalhos):
        nome_coluna = str(nome_coluna).strip()
        
        # Aplicando a tradução das abreviações
        if nome_coluna in traducao_colunas:
            coluna_traduzida = traducao_colunas[nome_coluna]
            df_final[coluna_traduzida] = dados[indice].replace('', pd.NA)
        elif nome_coluna in colunas_completas:
            df_final[nome_coluna] = dados[indice].replace('', pd.NA)
    
    # Garantindo que todas as colunas estejam presentes
    for coluna in colunas_completas:
        if coluna not in df_final.columns:
            df_final[coluna] = pd.NA
    
    # Limpeza final dos dados, se tiver linhas totalmente vazias
    df_final = df_final.dropna(how='all').replace('', pd.NA)
    
    # Ordenando as colunas conforme especificado
    return df_final[colunas_completas]

def salvar_resultados(dataframe):
    print("Salvando resultados...")
    
    
    # Salvando o CSV
    caminho_csv = os.path.join(pasta_saida, nome_csv)
    dataframe.to_csv(
        caminho_csv,
        index=False,
        encoding='utf-8-sig',
        sep=',',
        na_rep='NULL'
    )
    print(f"Arquivo CSV salvo em: {caminho_csv}")
    
    # Criando o arquivo ZIP
    caminho_zip = os.path.join(pasta_saida, nome_zip)
    with ZipFile(caminho_zip, 'w') as arquivo_zip:
        arquivo_zip.write(caminho_csv, os.path.basename(caminho_csv))
    print(f"Arquivo ZIP criado em: {caminho_zip}")
    
    return caminho_zip

if __name__ == "__main__":
    print("Inicio do Processo ")
    
    try:
        # Extração dos dados
        dados_extraidos = extrair_dados_pdf()
        
        # Processamento dos dados
        dados_processados = processar_dados(dados_extraidos)
        
        # Geração dos arquivos de saída
        arquivo_final = salvar_resultados(dados_processados)
        
        print("\nProcesso concluído com sucesso!")
        print(f"Arquivo gerado: {arquivo_final}")
        
    except Exception as erro:
        print(f"\nOcorreu um erro durante a execução: {str(erro)}")
    
    print("Fim do Processo ")