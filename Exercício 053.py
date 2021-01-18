print (40*'-')
centra = 'Verificador de palíndromo'
print (centra.center(40))
print (40*'-')

palavra = input('Digite a frase: ').upper().strip().replace(' ', '')
reverso = palavra[::-1]
print (f'O inverso de {palavra} é {reverso}')
if palavra == reverso:
    print ('A palavra é um palíndromo')
else:
    print ('A palavra NÃO é um palíndromo')

'''
inverso = ''
for n in range (len(palavra) -1, -1, -1):
    inverso = inverso + palavra[n]

print ('O inverso de {} é {}'.format (palavra, inverso, end=''))
if palavra == inverso:
    print ('A palavra é um palíndromo')
else:
    print ('A palavra NÃO é um palíndromo')
'''