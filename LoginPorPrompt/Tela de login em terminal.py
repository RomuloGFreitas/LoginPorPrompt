print("Bem-Vindo")
allusers = {}
def initial_choice():
    user_choice = True
    decision = '0'
    while user_choice:
        print("O que deseja fazer?:")
        print("1 - Logar-se\n2 - Cadastrar-se\n0 - Sair \n")
        decision = input(str('escolha uma opção:\n'))
        if decision == '0':   # Sair  
            break
        elif decision == '1': # Login
            login()    
        elif decision == '2': # cadastro de usuarios
            register()
        elif decision == 'admin':
            print(allusers)
        else:
            print('Insira uma opção valida!!\n')

    return

def login():
    try:
        usr = input("Insira seu usuário:\n")        
        pswrd = input("Insira sua senha:\n")
        request_login = {usr : pswrd}
        for request_login in allusers:
            break
        else:
            print("Usuário ou senha inválidos!")
            print("Tente novamente ou crie um novo usuário:")
            initial_choice()
    except:      
        print("parabens")


def register():
    usr = input("Insira um novo usuario:\n")
    pswrd = input("Insira uma nova senha:\n")
    allusers = {usr : pswrd}
    
    print("Registrado com sucesso!")
    return initial_choice()

initial_choice()

print("Sucesso, voce está logado!")