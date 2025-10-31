import os
from pathlib import Path

def criar_arquivo_csv_livros():
    """
    Cria e preenche o arquivo 'meus_livros.csv' com dados de livros.
    """
    
    NOME_ARQUIVO = "meus_livros.csv"
    caminho_completo = Path.cwd() / NOME_ARQUIVO
    
    # 1. Definindo os dados (você pode substituir esta lista pelos seus 10 livros)
    # Formato: (Título, Autor, Ano, Páginas)
    dados_livros = [
        ("O Caçador de Pipas", "Khaled Hosseini", 2003, 368),
        ("Torto Arado", "Itamar Vieira Junior", 2019, 264),
        ("1984", "George Orwell", 1949, 328),
        ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96),
        ("Ensaio sobre a Cegueira", "José Saramago", 1995, 310),
        ("Dom Casmurro", "Machado de Assis", 1899, 304),
        ("Cem Anos de Solidão", "Gabriel García Márquez", 1967, 417),
        ("Crime e Castigo", "Fiódor Dostoiévski", 1866, 545),
        ("Sapiens: Uma Breve História da Humanidade", "Yuval Noah Harari", 2011, 464),
        ("O Alienista", "Machado de Assis", 1882, 112),
    ]
    
    # 2. Abrindo o arquivo para escrita ('w') com o gerenciador 'with'
    try:
        # Usamos 'w' para garantir que criamos um arquivo novo (ou sobrescrevemos o existente)
        with open(caminho_completo, 'w', encoding='utf-8') as arquivo_csv:
            
            # 3. Escrevendo o cabeçalho
            cabecalho = "Título,Autor,Ano de publicação,Número de páginas\n"
            arquivo_csv.write(cabecalho)
            
            # 4. Escrevendo os dados de cada livro
            for titulo, autor, ano, paginas in dados_livros:
                # Converte todos os valores para string, junta-os com vírgula e adiciona quebra de linha
                linha = f"{titulo},{autor},{ano},{paginas}\n"
                arquivo_csv.write(linha)
                
        print(f"✅ Arquivo '{NOME_ARQUIVO}' criado e salvo com sucesso em: {caminho_completo.resolve()}")
        print("\nAgora você pode abri-lo com o Google Sheets, Excel ou outra ferramenta de planilha!")
        
    except Exception as e:
        print(f"❌ Ocorreu um erro ao criar o arquivo CSV: {e}")

# Executa a função
criar_arquivo_csv_livros()
