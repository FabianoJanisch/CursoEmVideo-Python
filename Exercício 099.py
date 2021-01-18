from random import randint
import time

def maior(*n):
    maior = c = 0
    for j in n:
        if c == 0:
            maior = j
        if j > maior:
            maior = j
        c +=1
    print (f'O maior números entre os números {n} é {maior}')


def maior2(*num):
    c = maior = 0
    print (40*'-')
    print('Analisando os valores informados...')
    alea = randint(1, 8)
    while c < alea:
        sorteio = randint(1, 10)
        print (sorteio, end = ' ', flush=True)
        if c == 0:
            maior = sorteio
        if sorteio > maior:
            maior = sorteio
        c += 1
        time.sleep(0.4)
    print (f'Foram informados {alea} números')
    print (f'O maior número informado foi {maior}')
    print (40*'-')
    print ()
    time.sleep(3)





maior(3, 5, 7, 2)
maior(3, 7, 9, 1)

maior2()
