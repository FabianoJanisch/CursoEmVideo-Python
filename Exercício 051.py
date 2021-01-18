print (40*'-')
centra = '10 termos de uma PA'
print (centra.center(40))
print (40*'-')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão do termo: '))

soma = 0 + termo - razao
for n in range(1, 11):
    soma = soma + razao
    print (soma, end = ' → ')
print ('Acabou')
