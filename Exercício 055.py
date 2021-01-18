lista = []
for p in range (1, 5+1):
    peso = float(input(f'Peso da {p}° pessoa em kg: '))
    lista = lista + [peso]
    listao = sorted(lista)

print ('O maior peso foi {:.1f}kg\nO menor peso foi {:.1f}kg'.format (listao[0], listao[-1]))
