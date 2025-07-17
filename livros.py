# função cadastrar livros 
def cadastrar_livros(lista_livros): 
    #inputs livro - titulo - autor - ano publicação
    titulo = str(input("Título: "))  
    autor = str(input("Autor: ")) 
    ano_publi = int(input("Ano de pulicação: "))  
    # verificando se o livro já esta cadastrado
    for i in lista_livros: 
        if i["titulo"] == titulo: 
            print("O livro já está cadastrado!") 
            return
    # novo livro 
    novo_livro = { 
        "titulo":titulo,  
        "autor":autor,  
        "ano_publicação":ano_publi, 
        "disponibilidade": True} 
    # adicionando novo livro a lista dicionario 
    lista_livros.append(novo_livro) 
    print("\nLivro cadastrado!\n")
 
 
# função listar livros 
def acervo_de_livros(lista_livros):  
    # verificando se existe livros cadastrados na lista
    if not lista_livros:  
        print("Não existem livros cadastrados no momento!\n")
        return 
    # imprimindo livros que estão disponiveis 
    print("\nLivros disponíveis\n")
    for i in lista_livros: 
        if i["disponibilidade"] == True:  
                print(f"Titulo: {i["titulo"]}\nAutor: {i["autor"]} \nAno de publicação: {i["ano_publicação"]} \nDisponibilidade: Disponivél\n")
    print("\n------------------------------\n") 
    # imprimindo livros que não estão disponiveis 
    print("\nLivros indisponíveis\n")
    for i in lista_livros: 
        if i["disponibilidade"] == False:  
                print(f"Titulo: {i["titulo"]}\nAutor: {i["autor"]} \nAno de publicação: {i["ano_publicação"]} \nDisponibilidade: Indisponivél\n")
     
    