import random
from pathlib import Path

# Nomes dos arquivos de gabarito
NOME_ARQUIVO_FORCA = "gabarito_forca.txt"
NOME_ARQUIVO_ENFORCADO = "gabarito_enforcado.txt"
MAX_ERROS = 6 # Limite de tentativas (0 a 6 = 7 estágios do enforcado)

def carregar_palavra_secreta():
    """Lê o arquivo de palavras e retorna uma palavra aleatória."""
    caminho = Path.cwd() / NOME_ARQUIVO_FORCA
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            palavras = [p.strip().upper() for p in f.readlines() if p.strip()]
        
        if not palavras:
            print(f"Erro: O arquivo '{NOME_ARQUIVO_FORCA}' está vazio.")
            return None
            
        return random.choice(palavras)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{NOME_ARQUIVO_FORCA}' não encontrado.")
        return None

def carregar_enforcado():
    """Lê o arquivo de gabarito_enforcado.txt e retorna uma lista de strings."""
    caminho = Path.cwd() / NOME_ARQUIVO_ENFORCADO
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            
        # Divide o conteúdo em estágios, separando pelas linhas em branco
        # O padrão '\n\n' assume que há uma linha em branco entre cada estágio
        estagios = [estagio.strip() for estagio in conteudo.split('\n\n') if estagio.strip()]
        
        # O jogo tem 6 erros, o que significa 7 estágios (0 a 6)
        if len(estagios) != MAX_ERROS + 1:
            print(f"Aviso: O arquivo '{NOME_ARQUIVO_ENFORCADO}' deve conter {MAX_ERROS + 1} estágios.")
            
        return estagios
    except FileNotFoundError:
        print(f"Erro: Arquivo '{NOME_ARQUIVO_ENFORCADO}' não encontrado.")
        return []

def imprime_enforcado(erros, estagios):
    """Imprime o estágio do enforcado baseado no número de erros."""
    if 0 <= erros < len(estagios):
        print(estagios[erros])
    else:
        # Caso o número de erros exceda o máximo (situação de Game Over)
        print(estagios[-1]) 

def jogar_forca():
    """Função principal para executar o Jogo da Forca."""
    
    palavra_secreta = carregar_palavra_secreta()
    estagios_enforcado = carregar_enforcado()
    
    if not palavra_secreta or not estagios_enforcado:
        print("Não foi possível iniciar o jogo devido a erros de arquivo.")
        return

    # Inicializa variáveis do jogo
    letras_certas = ['_'] * len(palavra_secreta)
    letras_erradas = []
    erros = 0
    palavra_completa = False

    print("===================================")
    print("      BEM-VINDO AO JOGO DA FORCA!  ")
    print("===================================")
    print(f"A palavra tem {len(palavra_secreta)} letras.")
    
    # Loop principal do jogo
    while erros < MAX_ERROS and not palavra_completa:
        
        print("\n" + "=" * 33)
        imprime_enforcado(erros, estagios_enforcado)
        print(f"Palavra: {' '.join(letras_certas)}")
        print(f"Erros ({erros}/{MAX_ERROS}): {' '.join(sorted(letras_erradas))}")
        print("-" * 33)

        # 1. Entrada do jogador
        tentativa = input("Digite uma letra (ou tente adivinhar a palavra): ").strip().upper()

        # 2. Validação da entrada
        if len(tentativa) == 1 and tentativa.isalpha():
            
            # Se a letra já foi tentada
            if tentativa in letras_certas or tentativa in letras_erradas:
                print(f"Você já tentou a letra '{tentativa}'. Tente outra.")
                continue

            # Processa a letra
            if tentativa in palavra_secreta:
                print("✅ Acertou a letra!")
                # Substitui os underscores pela letra acertada
                for i, letra_secreta in enumerate(palavra_secreta):
                    if letra_secreta == tentativa:
                        letras_certas[i] = tentativa
            else:
                print("❌ Errou a letra!")
                letras_erradas.append(tentativa)
                erros += 1

        # 3. Tentativa de adivinhar a palavra completa
        elif len(tentativa) > 1 and tentativa.isalpha():
            if tentativa == palavra_secreta:
                letras_certas = list(palavra_secreta) # Mostra a palavra completa
                palavra_completa = True
            else:
                print("❌ Tentativa de palavra errada!")
                erros = MAX_ERROS # Enforcamento instantâneo por tentativa errada da palavra
        
        else:
            print("Entrada inválida. Digite uma única letra ou a palavra completa.")

        # 4. Checa condição de vitória
        if '_' not in letras_certas:
            palavra_completa = True


    # --- Fim do Jogo ---
    print("\n" + "=" * 33)
    imprime_enforcado(erros, estagios_enforcado)
    print(f"A palavra era: {palavra_secreta}")

    if palavra_completa:
        print("\n🎉 PARABÉNS! VOCÊ VENCEU! 🎉")
    else:
        print("\n☠️ GAME OVER! VOCÊ FOI ENFORCADO! ☠️")
    print("=" * 33)

# Executa o jogo
jogar_forca()