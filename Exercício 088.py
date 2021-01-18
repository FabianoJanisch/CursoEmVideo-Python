from random import randint
import time
print (f'{"Jogo da megasena":-^50}'.upper())
jogos = int(input('Quantos jogos você quer jogar? '))
print ()
print (f'{f"Sorteando {jogos} jogos":_^50}')
for j in range (1, jogos+1):
    lista = []
    for n in range (1, 7):
        numbers = randint (1, 60)
        while True:
            if numbers not in lista:
                lista.append(numbers)
                break
            else:
                numbers = randint(1, 60)
    time.sleep(1)
    print (f'Jogo {j}: {sorted(lista)}')
print (50*'-')