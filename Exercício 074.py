from random import randint

lista = (randint(1, 10), randint(1, 10), randint(1, 10),
        randint(1, 10), randint(1, 10))
print (f'Os números sorteados foram: ', end ='')
for n in lista:
    print (n, end = ' ')
print (f'\nO menor valor sorteado foi {min(lista)}\nO maior valor sorteado foi {max(lista)}')

