# função cadatro de usuario 
def cadastro_usuario(lista_usuarios): 
    # inputs cadastro usuario - nome - CPF - pegou livro
    nome = str(input("Nome: ")).lower() 
    cpf_usuario = input("CPF: ") 
    # se o tamnho do cpf for diferetne de 11 será inválido
    if len(cpf_usuario) != 11: 
        print("\nO CPF deve conter 11 digitos! Tente novamente.\n") 
        return 
    # verificando se usuario já possui cadastro
    for i in lista_usuarios: 
        if i["CPF"] == cpf_usuario: 
            print("\nUsuário já possui cadastro\n")  
            return
    # novo usuario
    novo_usuario = { 
        "nome":nome,  
        "CPF":cpf_usuario,  
        "pegou_livro": False} 
    # adicionando um novo usuario na lista dicionario
    lista_usuarios.append(novo_usuario) 
    print("\nUsuário cadastrado com sucesso!\n")
