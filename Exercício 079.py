lista = list()
continuar2 = ' '
while True:
    valor = int(input('Digite um valor: ' ))
    if valor in lista:
        print ('Número já existe, não adicionado...')
    else:
        lista.append(valor)
        print ('Valor adicionado')
    continuar = input('Você deseja continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    if continuar != 'S':
        while True:
            continuar2 = input('Por favor, use somente as letras [S/N]').strip().upper()
            if continuar2 == 'N' or continuar2 == 'S':
                break
    if continuar2 in 'N':
        break
lista.sort()
print (f'Todos os valores únicos adicionados em ordem crescente é {lista}')

'''
if valor not in lista:
    lista.append(valor)
'''
