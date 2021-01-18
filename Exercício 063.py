'''
n = int(input('Quantos números da sequência de Fibonacci você deseja visualizar? '))

n1 = 0
n2 = 1
print (f'{n1} → {n2}', end = ' → ')
cont = 2
while cont < n:
    n3 = n1 + n2
    print (f'{n3}', end = ' → ')
    n1 = n2
    n2 = n3
    cont += 1
print ('FIM') 
'''

n1 = 0
n2 = 1

n = int(input('Quantos números da sequência de Fibonacci você deseja visualizar? '))
while n != 0:
    print (f'{n1}', end =' → ')
    n1 += n2
    n2 = n1 - n2
    n -= 1
print ('FIM')
