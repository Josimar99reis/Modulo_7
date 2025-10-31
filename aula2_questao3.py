import string # Usado para obter a lista de pontuações

def eh_palindromo(frase):
    """Verifica se uma frase é um palíndromo, ignorando espaços e pontuação."""
    
    # 1. Converte a frase para minúsculas
    frase_limpa = frase.lower()
    
    # 2. Remove pontuações e espaços em branco
    # Cria uma tabela de mapeamento onde todos os caracteres de pontuação e o espaço em branco são mapeados para None (remoção)
    tabela_remocao = str.maketrans('', '', string.punctuation + ' ')
    frase_limpa = frase_limpa.translate(tabela_remocao)
    
    # 3. Verifica se é um palíndromo
    # Compara a string limpa com sua versão invertida
    return frase_limpa == frase_limpa[::-1]

def verificador_palindromo():
    """Loop principal para verificar palíndromos."""
    print("--- Exercício 3 ---")
    while True:
        frase = input('Digite uma frase (digite "fim" para encerrar): ')
        
        # Condição de saída
        if frase.lower() == "fim":
            break
            
        if eh_palindromo(frase):
            print(f'"{frase}" é palíndromo\n')
        else:
            print(f'"{frase}" não é palíndromo\n')

# Chamada da função para testar o programa
verificador_palindromo()