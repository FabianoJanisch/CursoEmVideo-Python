import time
def contador(início, fim, passo):
    if passo < 0:
        passo = passo*-1
    if passo == 0:
        passo = 1
    if início < fim:
        print (35*'-')
        print (f'Contagem de {início} até {fim} com {passo} passos')
        for n in range(início, fim+1, passo):
            print (n, end = ' ', flush=True)
            time.sleep(0.5)
        print ()
        print (35*'-')
    else:
        c = início
        while c >= fim:
            print (c, end = ' ', flush=True)
            c -= passo
            time.sleep(0.5)


contador(1, 10, 1)
contador(10, 0, 2)
print (35*'-')
print ('Sua vez de personalizar a contagem')
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(início, fim, passo)
