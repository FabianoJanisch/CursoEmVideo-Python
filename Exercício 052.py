print (40*'-')
centra = 'Verificador de número primo'
print (centra.center(40))
print (40*'-')

soma = 0
soma2 = 0
numero = int(input('Digite aqui seu número: '))
for n in range (1, numero + 1):
    if numero % n == 0:
        print ('\33[33m', end='')
        soma = soma + 1
    else:
        print ('\33[31m', end='')
        soma2 = soma2 + 1
    print (f'{n} ', end = '')

if soma == 2:
    print (f'\n\33[mO número {numero} é\33[34m PRIMO\33[m pois é divisível somente {soma} vezes')
else:
    print (f'\n\33[mO número {numero} não é \33[34mPRIMO\33[m pois pode ser dividido por 3 ou mais números')