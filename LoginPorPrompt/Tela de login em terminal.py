print("Bem-Vindo")
def initialchoice():
    userchoice = True
    decision = '0'
    while userchoice:
        print("O que deseja fazer?:")
        print("0 - Sair \n1 - Logar-se\n2 - Cadastrar-se\n")
        decision = input(str('escolha uma opção:\n'))
        if decision == '0':   # Sair  
            break
        elif decision == '1': # Login
            pass    
        elif decision == '2': # cadastro de usuarios
            pass 
        else:
            print('Insira uma opção valida!!\n')


    
    return

#def

def register():


initialchoice()

