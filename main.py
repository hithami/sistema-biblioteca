# json 
import json  
# importanto modulos 
from livros import cadastrar_livros, acervo_de_livros  
from usuario import cadastro_usuario
from emprestimo import emprestimo_livro

# lista dicionario livros 
lista_livros = [ 
    
] 
#  lista dicionario usuarios
lista_usuarios = [ 
    {"nome": "Maria", "CPF": "12345678900", "pegou livro": True}
] 
 
# dados do arquivo json usuarios
try:
    with open("usuarios.json", "r") as arquivo_usuarios:
        lista_usuarios = json.load(arquivo_usuarios)  
except FileNotFoundError: 
    lista_usuarios = [] 

# dados do arquivo json livros 
try: 
    with open("livros.json", "r") as arquivo_livros: 
        lista_livros = json.load(arquivo_livros) 
except FileNotFoundError: 
    lista_livros = []
  
# Menu 
 
while True: 
    try: 
        resposta = int(input("1. Cadastrar Livro\n2. Cadastrar Usuário\n3. Listar Livros\n4. Realizar emprestimo\n5. Sair\n"))  
        # condições menu 
        if resposta == 1: 
            print("\nCadastrar Livro\n") 
            cadastrar_livros(lista_livros) 
            with open("usuarios.json", "w") as arquivo_usuarios:
                json.dump(lista_usuarios, arquivo_usuarios, indent=4)
            with open("livros.json", "w") as arquivo_livros:
                json.dump(lista_livros, arquivo_livros, indent=4)
        elif resposta == 2: 
            print("\nCadastrar Usuário\n") 
            cadastro_usuario(lista_usuarios) 
            with open("usuarios.json", "w") as arquivo_usuarios:
                json.dump(lista_usuarios, arquivo_usuarios, indent=4)
            with open("livros.json", "w") as arquivo_livros:
                json.dump(lista_livros, arquivo_livros, indent=4) 
        elif resposta == 3: 
            print("\nListar Livros\n") 
            acervo_de_livros(lista_livros) 
            with open("usuarios.json", "w") as arquivo_usuarios:
                json.dump(lista_usuarios, arquivo_usuarios, indent=4)
            with open("livros.json", "w") as arquivo_livros:
                json.dump(lista_livros, arquivo_livros, indent=4) 
        elif resposta == 4:  
            print("\nRealizar emprestimo\n")
            emprestimo_livro(lista_livros, lista_usuarios) 
            with open("usuarios.json", "w") as arquivo_usuarios:
                json.dump(lista_usuarios, arquivo_usuarios, indent=4)
            with open("livros.json", "w") as arquivo_livros:
                json.dump(lista_livros, arquivo_livros, indent=4) 
        elif resposta == 5: 
            print("Programa encerrado!") 
            break  
        else: 
            print("Resposta inválida! Tente novamente.") 
    except ValueError: 
        print("Valor informado inválido! Tente novamente")
        # json salvamento  
        with open("usuarios.json", "w") as arquivo_usuarios:
            json.dump(lista_usuarios, arquivo_usuarios)  
        with open("livros.json", "w") as arquivo_livros: 
            json.dump(lista_livros, arquivo_livros)
