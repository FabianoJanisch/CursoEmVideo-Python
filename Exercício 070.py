total = maior1000 = cont = menor = 0
while True:
    produto = input('Nome do produto: ')
    preço = int(input('Valor do produto: R$'))
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Você deseja continuar? [S/N] ').upper().strip()[0]
    total += preço
    cont += 1
    if preço > 1000:
        maior1000 +=1
    if cont == 1 or preço < menor:
        menor = preço
        produtom = produto
    if continuar == 'N':
        break
    print (40*'-')
print (40*'-')
print (f'O total gasto foi R${total}\nHá {maior1000} produtos que custam mais que R$1000\nO produto mais barato é o {produtom} e custa R${menor}')
print (40*'-')