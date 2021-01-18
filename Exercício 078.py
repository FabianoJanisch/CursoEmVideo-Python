posiçãomaior = []
posiçãomenor = []
lista = []
for l in range(0,5):
    lista.append(int(input(f'Digite aqui o valor da posição {l}: ')))
ordenado = sorted(lista)
for posição, valores in enumerate(lista):
    if valores == max(lista):
        posiçãomaior.append(posição)
    if valores == min(lista):
        posiçãomenor.append(posição)
print (f'Você digitou os valores {lista}')
print (f'O maior valor digitado foi {ordenado[-1]} nas posições {posiçãomaior} ')
print (f'O menor valor digitado foi {ordenado[0]} nas posições {posiçãomenor}')
