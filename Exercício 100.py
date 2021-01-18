from random import randint
import time
números = []
def sorteia(*num):
    c = 0
    print (f'Foi sorteado na lista os 5 números: ', end = '')
    while c < 5:
        s = randint(1, 10)
        números.append(s)
        c += 1
        print (s, end = ' ', flush=True)
        time.sleep(0.4)


def somaPar():
    par = 0
    for p in números:
        if p % 2 == 0:
            par += p
    print (f'\nSomando os valores pares da lista {números}, a soma é {par}')


sorteia()
somaPar()
