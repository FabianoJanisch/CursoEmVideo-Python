lista = list()
listai = list()
listap = list()
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        continuar = input('Você deseja adicionar mais um número? [S/N] ').strip().upper()
        if continuar in 'N':
            break
        if continuar in 'S':
            break
        if continuar != 'S':
            print('Por favor, digite novamente ')
    if continuar in 'N':
        break
for num in range (0, len(lista)):
    if lista[num] % 2 == 0:
        listap.append(lista[num])
    else:
        listai.append(lista[num])
print (f'A lista inteira é {lista}')
print (f'A lista ímpar é {listai}')
print (f'A lista par é {listap}')

