import re

def validador_senha(senha):
    """
    Verifica se uma senha atende aos seguintes critérios:
    1. Pelo menos 8 caracteres.
    2. Contém pelo menos uma letra maiúscula e uma minúscula.
    3. Contém pelo menos um número.
    4. Contém pelo menos um caractere especial (@, #, $, etc.).
    """
    
    # 1. Pelo menos 8 caracteres de comprimento
    if len(senha) < 8:
        return False
        
    # 2. Contém pelo menos uma letra maiúscula e uma letra minúscula
    # 3. Contém pelo menos um número
    # 4. Contém pelo menos um caractere especial (usando regex para simplificar)
    
    # Pelo menos uma minúscula: (?=.*[a-z])
    # Pelo menos uma maiúscula: (?=.*[A-Z])
    # Pelo menos um número: (?=.*[0-9])
    # Pelo menos um caractere especial (não alfanumérico, nem sublinhado): (?=.*[^a-zA-Z0-9\s])
    # Obs: O ^ no regex significa "qualquer coisa exceto"
    
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^a-zA-Z0-9\s]).{8,}$"
    
    return bool(re.search(regex, senha))

# Exemplo de uso:

print("--- Exercício 4 ---")
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(f'"{senha1}" é válida? {validador_senha(senha1)}') # Saída esperada: True
print(f'"{senha2}" é válida? {validador_senha(senha2)}') # Saída esperada: False
print(f'"{senha3}" é válida? {validador_senha(senha3)}') # Saída esperada: False
print(f'{"TESTE123"} é válida? {validador_senha("TESTE123")}') # Saída esperada: False (faltam minúsculas e especial)
print(f'{"aB1@"} é válida? {validador_senha("aB1@")}') # Saída esperada: False (menos de 8 caracteres)