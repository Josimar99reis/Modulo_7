import os
import re
from pathlib import Path

def processar_frase_para_palavras():
    """
    Lê 'frase.txt', remove caracteres não alfabéticos e espaços,
    salva cada palavra em uma nova linha em 'palavras.txt' e imprime seu conteúdo.
    """
    
    nome_arquivo_entrada = "frase.txt"
    nome_arquivo_saida = "palavras.txt"
    
    # Define os caminhos completos
    diretorio_atual = Path.cwd()
    caminho_entrada = diretorio_atual / nome_arquivo_entrada
    caminho_saida = diretorio_atual / nome_arquivo_saida
    
    # --- Passo de Simulação (Para garantir que o frase.txt exista para este teste) ---
    # Se 'frase.txt' não existir, vamos criá-lo com um exemplo padrão
    if not caminho_entrada.exists():
        print(f"Arquivo '{nome_arquivo_entrada}' não encontrado. Criando com texto de exemplo.")
        texto_exemplo = "Bom dia, meu nome é Davi."
        try:
            with open(caminho_entrada, 'w', encoding='utf-8') as f:
                f.write(texto_exemplo)
        except Exception as e:
            print(f"Erro ao criar arquivo de exemplo: {e}")
            return
    # --------------------------------------------------------------------------------
    
    texto_lido = ""
    
    # 1. Leitura do arquivo 'frase.txt'
    try:
        with open(caminho_entrada, 'r', encoding='utf-8') as arquivo_in:
            texto_lido = arquivo_in.read()
            print(f"Conteúdo lido de '{nome_arquivo_entrada}': '{texto_lido.strip()}'")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo_entrada}' não foi encontrado no diretório atual.")
        return
    except Exception as e:
        print(f"Ocorreu um erro durante a leitura: {e}")
        return
        
    # 2. Processamento do texto
    
    # Remove todos os caracteres não alfabéticos (mantém letras e espaços)
    # [a-zA-Z\s] significa: qualquer letra (a-z, A-Z) ou espaço (\s)
    # O ^ inverte a seleção: remove TUDO O QUE NÃO FOR letra ou espaço. (ex: vírgulas, pontos)
    texto_sem_nao_alfabeticos = re.sub(r'[^a-zA-ZáàâãéèêíìîóòôõúùûÁÀÂÃÉÈÊÍÌÎÓÒÔÕÚÙÛ\s]', '', texto_lido)
    
    # Quebra o texto em uma lista de palavras usando espaços em branco como delimitador
    # O método split() sem argumentos lida com múltiplos espaços e quebras de linha
    palavras_list = texto_sem_nao_alfabeticos.split()
    
    # Prepara o conteúdo a ser salvo (cada palavra seguida por uma quebra de linha)
    conteudo_saida = "\n".join(palavras_list)
    
    # 3. Salva no arquivo 'palavras.txt'
    try:
        with open(caminho_saida, 'w', encoding='utf-8') as arquivo_out:
            arquivo_out.write(conteudo_saida)
            
        print(f"\nDados processados e salvos em '{nome_arquivo_saida}'.")
        
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")
        return
        
    # 4. Imprime o conteúdo do novo arquivo
    print("\n--- Conteúdo do 'palavras.txt' ---")
    print(conteudo_saida)
    print("----------------------------------\n")


# Executa a função
processar_frase_para_palavras()