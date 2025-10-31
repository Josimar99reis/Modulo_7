import os
from pathlib import Path

def salvar_frase_e_imprimir_caminho():
    """
    Solicita uma frase do usuário, salva-a em 'frase.txt' no diretório atual
    e imprime o caminho completo do arquivo.
    """
    
    # 1. Solicita a frase do usuário
    frase_usuario = input("Digite uma frase: ")
    
    # 2. Define o nome do arquivo
    nome_arquivo = "frase.txt"
    
    # Obtém o diretório atual onde o script está sendo executado
    # Path.cwd() retorna o Current Working Directory (Diretório de Trabalho Atual)
    diretorio_atual = Path.cwd()
    
    # Cria o caminho completo para o arquivo
    caminho_completo_arquivo = diretorio_atual / nome_arquivo
    
    try:
        # 3. Salva a frase no arquivo
        # 'w' abre o arquivo para escrita (sobrescreve se existir)
        # O gerenciador de contexto 'with open(...) ' garante que o arquivo seja fechado
        with open(caminho_completo_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(frase_usuario)
            
        # 4. Imprime o caminho completo do arquivo salvo
        # str(caminho_completo_arquivo.resolve()) garante o caminho absoluto e limpo
        caminho_impresso = str(caminho_completo_arquivo.resolve())
        
        print(f"Frase salva em {caminho_impresso}")
        
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")

# Executa a função
salvar_frase_e_imprimir_caminho()