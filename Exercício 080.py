lista = []
for n in range(0, 5):
    valor = int(input('Digite um número: '))
    if n == 0:
        lista.append(valor)
        print ('Número adicionado no final da lista')
    elif valor > lista[-1]:
        lista.append(valor)
        print ('Número adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print (f'Número adicionado na posição {pos}')
                break
            pos += 1

print (f'Os números digitados em ordem foi {lista}')