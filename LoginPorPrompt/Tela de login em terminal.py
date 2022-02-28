"""print('Bem-Vindo\n')

while True:
    user = input(str('Usuário\n'))
    password = input('Senha')

    break
"""

userchoice = True

input(str("Escolha umna opção: \n1 - Logar-se\n2 - Cadastrar-se"))
while userchoice:
    des = input('escolha uma opção')
    tipo = type(des)
    if des == '0':
        n = False
    print (tipo)
