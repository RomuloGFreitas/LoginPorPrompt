print("Bem-Vindo")
def initialchoice():
    userchoice = True
    while userchoice:
        print("O que deseja fazer?: \n0 - Sair \n1 - Logar-se\n2 - Cadastrar-se\n")
        descision = input(str('escolha uma opção:\n'))
        if descision == '0':
            break
    
    return
initialchoice()
