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


def leiaFloat(num): 
    while True:
        try:
            numero = float(input(num))
        except (ValueError, TypeError):
            print ('\33[31mErro! Digite um número inteiro válido\33[m')
        except (KeyboardInterrupt):
            print ('\33[31mO usuário não digitou os dados\33[m')
            return 0
        else:
            return numero


n = leiaInt('Digite um número inteiro: ')
nf = leiaFloat('Digite um número real: ')
print (f'Você digitou o número inteiro {n} e número real {nf}')
