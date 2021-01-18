n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
n3 = int(input('Digite o 3° valor: '))
n4 = int(input('Digite o 4° valor: '))

tupla = (n1, n2, n3, n4)
print (f'\nOs números digitados foram {tupla}')
print (f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print (f'O número 3 apareceu pela primeira vez na posição {tupla.index(3)+1}')
else:
    print ('O número 3 não foi digitado')
print (f'Os números pares digitados foram: ', end = '')
count = 0
for p in tupla:
    if p % 2 == 0:
        print (p, end = ' ')
        count =+ 1
if count == 0:
    print (0)

'''
lista = []
for p in tupla:
    if p % 2 == 0:
        lista += [p]
print (f'Os números pares digitados foram: {lista}')
'''