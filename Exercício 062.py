print (40*'-')
centra = 'Termos de uma PA'
print (centra.center(40))
print (40*'-')

termo = int(input('Primeiro termo: '))
razão = int(input('Razão do termo: '))

soma = 0 + termo - razão
cont = 0
máximo = 10
while cont < máximo:
    soma = soma + razão
    print (soma, end = ' → ')
    cont += 1
    if cont == máximo:
        print ('Pausa')
        mais = int(input('Quantos termos você quer mostrar a mais? '))
        máximo += mais
print (f'Foi mostrado {máximo} termos')
print ('Fim')
