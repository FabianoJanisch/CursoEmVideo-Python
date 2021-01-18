
print (40*'-')
centra = '10 termos de uma PA'
print (centra.center(40))
print (40*'-')

termo = int(input('Primeiro termo: '))
razão = int(input('Razão do termo: '))

soma = 0 + termo - razão
cont = 0
while cont < 10:
    soma = soma + razão
    print (soma, end = ' → ')
    cont += 1
print ('Fim')