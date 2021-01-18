from math import factorial

fatorialn = int(input('Digite um número para calcular seu fatorial: '))
contagem = fatorialn
f = 1
print (f'O fatorial de {fatorialn}! = ', end='')
while contagem > 0:
    print ('{}'.format (contagem), end='')
    print (' x ' if contagem > 1 else ' = ', end='')

    f *= contagem    
    contagem -= 1
print (f'{f}')

'''
numero = int(input('Digite aqui seu fatorial: '))
print (f'O fatorial de {numero}! é ', end='')
for f in range (numero, -1, -1):
    print (f'{f}' if f > 0 else '', end ='')
    print (' x ' if f > 0 else '= ', end ='')

print (factorial(numero))
'''