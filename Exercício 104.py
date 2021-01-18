def leiaInt(num):
    while True:
        numero = input(num)
        if numero.isnumeric():
            return numero
        else:
            print ('\33[31mErro! Digite um número inteiro válido\33[m')


#Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
