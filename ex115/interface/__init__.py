def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\33[31mErro! Digite um número real válido\33[m')
            continue
        except KeyboardInterrupt:
            print('\33[31mO Usuário não digitou os dados\33[m')
            return 0
        else:
            return n


def opção(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            return int(num)
        else:
            print ('\33[31mErro! Digite um número de 1 a 3\33[m')


def início():
    print (30*'-')
    print ('Menu principal'.center(30))
    print (30*'-')
    print ('''\033[33m1 -\033[m \033[34mVer pessoas cadastradas\033[m
\033[33m2 -\033[m \033[34mCadastrar nova pessoas\033[m
\033[33m3 -\033[m \033[34mSair do sistema\033[m''')
    print (30*'-')

