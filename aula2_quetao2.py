def substituir_vogais():
    """Solicita uma frase e substitui todas as vogais por '*'."""
    
    frase_original = input("Digite uma frase: ")
    frase_modificada = ""
    # Define o conjunto de vogais (maiúsculas e minúsculas)
    vogais = "aeiouAEIOUáéíóúÁÉÍÓÚãõÃÕâêîôûÂÊÎÔÛàèìòùÀÈÌÒÙ"
    
    for caractere in frase_original:
        if caractere in vogais:
            frase_modificada += "*"
        else:
            frase_modificada += caractere
            
    print(f'\nFrase modificada: {frase_modificada}\n')

# Chamada da função para testar o programa
print("--- Exercício 2 ---")
substituir_vogais()