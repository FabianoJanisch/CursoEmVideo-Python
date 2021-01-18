lista = [[], []]
for n in range (1, 8):
    numeros = int(input(f'Digite o {n}° número: '))
    if numeros % 2 == 1:
        lista[0].append(numeros)
    if numeros % 2 == 0:
        lista[1].append(numeros)

print (f'Os números ímpares digitados foram {sorted(lista[0])} ')
print (f'Os números pares digitados foram {sorted(lista[1])} ')

'''
print ('Os números ímpares digitados foram ', end = '')
for i in lista:
    if i % 2 == 1:
        print (f'[{i}] ', end = '')
print ('\nOs números pares digitados foram ', end = '')
for i in lista:
    if i % 2 == 0:
        print (f'[{i}] ', end = '')
'''

