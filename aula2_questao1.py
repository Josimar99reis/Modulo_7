def data_por_extenso():
    """Solicita a data de nascimento e a imprime com o nome do mês por extenso."""
    
    # Lista dos nomes dos meses (índice 0 não é usado para que o índice 1 corresponda a Janeiro)
    meses = [
        "", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    
    while True:
        data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")
        
        # Verifica se a data tem o formato esperado 'dd/mm/aaaa'
        if len(data_nascimento) == 10 and data_nascimento[2] == '/' and data_nascimento[5] == '/':
            try:
                # Extrai dia, mês e ano
                dia = data_nascimento[0:2]
                mes_num = int(data_nascimento[3:5])
                ano = data_nascimento[6:10]
                
                # Verifica se o número do mês é válido
                if 1 <= mes_num <= 12:
                    mes_extenso = meses[mes_num]
                    print(f'\nVocê nasceu em  {dia} de {mes_extenso} de {ano}.\n')
                    break
                else:
                    print("Erro: O número do mês deve estar entre 01 e 12. Tente novamente.")
            except ValueError:
                print("Erro: A data deve conter números para dia, mês e ano. Tente novamente.")
        else:
            print("Erro: Formato de data inválido. Use dd/mm/aaaa. Tente novamente.")

# Chamada da função para testar o programa
print("--- Exercício 1 ---")
data_por_extenso()