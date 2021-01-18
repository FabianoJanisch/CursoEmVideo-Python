n1 = int(input('Digite aqui seu primeiro número inteiro '))
n2 = int(input('Digite aqui seu segundo número inteiro '))
organização = [n1, n2]

nmaior = max(organização)
nmenor = min(organização)

'''
lista = sorted(organização)
nmaior = lista[-1]
nmenor = lista[0]
'''
if nmaior == nmenor:
    print ('Não existe valor maior, os dois números são iguais')
if n1 > n2:
    print ('O primeiro valor é maior')
if n2 > n1:
    print ('O segundo valor é maior')

