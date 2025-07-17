import time 
def emprestimo_livro(lista_livros, lista_usuarios):  
    while True: 
        # try: 
            resposta = int(input("1. Alugar livro\n2. Devolver livro\n3. Sair\n")) 
            # alugar  livro  
            if resposta == 1: 
                # pedindo cpf do usuario para verificar na lista dicionario se ele esta cadastrado 
                cpf_do_usuario = input("\nCPF do Usuário: ")  
                usuario_encontrado = False #flag 

                for usuario in lista_usuarios: 
                    if cpf_do_usuario == usuario["CPF"]:
                        print("Cadastro encontrado!") 
                        usuario_encontrado = True 
                        time.sleep(2) 

                        # verificando se usuario possui livro em emprestimo 
                        if usuario["pegou_livro"] == False: 
                            print("Possui livro alugado: Não")   

                            # verificando se livro que usuario quer está disponivel 
                            livro_aluguel = input("Titulo do livro: ").lower().strip() 
                            livro_encontrado = False #flag
                            for livro in lista_livros: 
                                if livro_aluguel == livro["titulo"].lower() and livro["disponibilidade"] == True: 
                                    print("livro encontrado!") 
                                    livro_encontrado = True #flag
                                    time.sleep(2) 
                                    #  alugando  
                                    print("\nLivro alugado com sucesso!\n") 
                                    usuario["pegou_livro"] = True #usuario
                                    livro["disponibilidade"] = False #livro
                                    break
                                     
                            if not livro_encontrado: 
                                print("Livro indisponivel! Escolha outro livro.") 
                                continue
                                    
                        else: 
                            print("Possui ivro em emprestimo: Sim\nDevolva o livro para um novo aluguel!") 
                            break
                if not usuario_encontrado:
                    print("Usuário não cadastrado!\nFaça seu cadastro :D") 
                    break 
             
            # devolver livro 
            elif resposta == 2: 
                # pedindo cpf do usuario para verificar na lista dicionario se ele esta cadastrado 
                cpf_do_usuario = input("\nCPF do Usuário: ") 
                usuario_encontrado = False #flag 
                 
                # procurando usuario 
                for usuario in lista_usuarios: 
                    if cpf_do_usuario == usuario["CPF"]: 
                        print("Usuário encontrado!\n") 
                        usuario_encontrado = True 
                        time.sleep(2)  
                         
                        #verificando se usuario pegou livro 
                        if usuario["pegou_livro"] == True: 
                            print("Possui livro alugado: Sim") 
                             
                            #verificando qual livro o usuario quer devolver 
                            livro_devolucao = input("Titulo do livro: ").lower().strip() 
                            livro_encontrado = False #flag
                            for livro in lista_livros: 
                                if livro_devolucao == livro["titulo"].lower() and livro["disponibilidade"] == False: 
                                    print("Livro alugado encontrado!\n") 
                                    livro_encontrado = True #flag 
                                    time.sleep(2)  
                                    #devolvendo  
                                    print("\nDevolução concluida!\n") 
                                    usuario["pegou_livro"] = False  
                                    livro["disponibilidade"] = True 

                            if not livro_encontrado: 
                                print("Livro não encontrado!")

                        else: 
                            print("Possui livro alugado: Não") 
                            print("Você não possui nenhum livro alugado no momento.\n") 
                            break
                         
                #não tem livro em emprestimo 
                if not usuario_encontrado: 
                    print("O usuário não encontrado.") 
                    break
            # sair 
            elif resposta == 3: 
                break
