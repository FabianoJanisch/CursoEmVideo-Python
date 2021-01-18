ano = int(input('Escreva aqui o ano que você acha que é bissexto '))
conta = ano % 4
if conta == 0:
    print (f'O ano de {ano} é bissexto :)')
else:
    print (f'O ano de {ano} não é bissexto ')
