import time
v = False
v1 = int(input('Digite o 1° número: '))
v2 = int(input('Digite o 2° número: '))

c1 = '\033[34m'
c2 = '\033[m'
while not v:
    print (f'{c1}[ 1 ]{c2} somar\n{c1}[ 2 ]{c2} multiplicar\n{c1}[ 3 ]{c2} Maior\n{c1}[ 4 ]{c2} Novos números\n{c1}[ 5 ]{c2} Sair do programa')
    resposta = int(input(''))
    if resposta == 1:
        soma = v1 + v2
        print ('A soma de {} + {} é {}'.format (v1, v2, soma))
        time.sleep(2)
    elif resposta == 2:
        mult = v1*v2
        print ('A multiplicação de {} x {} é {}'.format (v1, v2, mult))
        time.sleep(2)
    elif resposta == 3:
        if v1 > v2:
            print (f'O 1° número {v1} é maior que o 2° número {v2}')
        elif v2 > v1:
            print (f'O 2° número {v2} é maior que o 1° número {v1}')
        elif v1 == v2:
            print (f'Os dois números são iguais')
        time.sleep(2)
    elif resposta == 4:
        v1 = int(input('Digite o 1° número novamente: '))
        v2 = int(input('Digite o 2° número novamente: '))
    elif resposta == 5:
        print ('Obrigado pela preferência, volte sempre :)')
        v = True
    else:
        print ('Esse número não existe, digite entre 1 e 5')
        time.sleep(2)
    print (30*'-')
