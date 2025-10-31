import re
from pathlib import Path

def analisar_roteiro_estomago():
    """
    Abre o arquivo 'estomago.txt', realiza a análise do texto
    e imprime as informações solicitadas.
    """
    
    nome_arquivo = "estomago.txt"
    caminho_arquivo = Path.cwd() / nome_arquivo
    
    try:
        # Abre o arquivo para leitura
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            # Lê todas as linhas do arquivo em uma lista
            linhas = arquivo.readlines()
            
    except FileNotFoundError:
        print(f"❌ ERRO: O arquivo '{nome_arquivo}' não foi encontrado no diretório atual.")
        print("Certifique-se de que você baixou o roteiro e o salvou como 'estomago.txt'.")
        return
    except Exception as e:
        print(f"❌ Ocorreu um erro ao ler o arquivo: {e}")
        return

    # --- 1. O número de linhas do arquivo ---
    num_linhas = len(linhas)
    print("==================================================")
    print(f"Número total de linhas do arquivo: {num_linhas}\n")
    
    # --- 2. O texto das primeiras 25 linhas ---
    print("--- PRIMEIRAS 25 LINHAS DO ROTEIRO ---")
    # Usa slice [:25] para pegar as 25 primeiras linhas
    for i, linha in enumerate(linhas[:25]):
        # Imprime o número da linha e a linha, removendo espaços e quebras de linha ('strip()')
        print(f"Linha {i+1:02}: {linha.strip()}")
    print("--------------------------------------\n")
    
    # --- 3. A linha com maior número de caracteres ---
    
    # Encontra o comprimento da linha mais longa
    # 'max(..., key=len)' encontra o item de maior comprimento na lista
    linha_mais_longa = max(linhas, key=len)
    
    # Remove espaços e quebras de linha antes de contar o comprimento para exibição
    comprimento_max = len(linha_mais_longa.strip())
    
    # Encontra o índice (número da linha) da linha mais longa
    indice_linha_mais_longa = linhas.index(linha_mais_longa) + 1
    
    print("--- LINHA COM MAIOR NÚMERO DE CARACTERES ---")
    print(f"Comprimento: {comprimento_max} caracteres")
    print(f"Linha Nº: {indice_linha_mais_longa}")
    print(f"Conteúdo: {linha_mais_longa.strip()}\n")
    
    # --- 4. O número de menções aos personagens "Nonato" e "Íria" ---
    
    # Converte todo o texto para uma única string e minúsculas para facilitar a contagem
    texto_completo = "".join(linhas).lower()
    
    # Define os padrões de busca (usando regex para garantir que seja a palavra inteira)
    
    # Padrão para Nonato: \bnonato\b (limites de palavra garantem que 'nonato' não seja parte de outra)
    padrao_nonato = r'\bnonato\b'
    
    # Padrão para Íria: \bíria\b ou \biria\b (incluindo a variação sem acento, já que o texto foi convertido para minúsculas)
    # Obs: Se o texto original não tiver o 'Í', a busca deve ser flexível.
    # Usaremos uma busca simples por 'iria' e 'nonato' com limites de palavra.
    
    # Regex flexível para 'Íria' (com ou sem acento, com limite de palavra)
    padrao_iria_flex = r'\bíria\b|\biria\b' 

    # Conta as ocorrências usando re.findall
    contagem_nonato = len(re.findall(padrao_nonato, texto_completo))
    contagem_iria = len(re.findall(padrao_iria_flex, texto_completo))
    
    print("--- CONTAGEM DE PERSONAGENS (Palavras Inteiras) ---")
    print(f'Menções a "Nonato": {contagem_nonato}')
    print(f'Menções a "Íria":   {contagem_iria}')
    print("==================================================")


# Executa a função de análise
analisar_roteiro_estomago()