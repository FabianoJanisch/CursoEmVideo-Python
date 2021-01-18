lista = []
while True:
    n = lista.append(int(input('Digite um número: ')))
    while True:
        continuar = input('Você deseja adicionar mais um número? [S/N] ').upper().strip()
        if continuar in 'N':
            break
        if continuar in 'S':
            break
        if continuar != 'S':
            print ('Por favor, digite novamente')
    if 'N' in continuar:
        break

print (f'\nForam digitados {len(lista)} números')
lista.sort(reverse=True)
print (f'A lista em ordem descrecente é {lista}')
if 5 in lista:
    print ('O valor 5 está na lista')
elif 5 not in lista:
    print ('O valor 5 não está presente na lista')


'''
if valor not in lista:
    lista.append(valor)'''
