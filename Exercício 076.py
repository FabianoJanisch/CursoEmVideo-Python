lista = ('Tortuguita', 9.90, 'Melancia', 6.75,
        'Caderno', 5.50, 'Lâmpada', 15.90,
        'T', 4.99, 'Garrafa de vidro', 23.90)

print (60*'-')
print (f'{"Lista de preços mercadinho bambu":^60}')
print (60*'-')

for p in lista:
    if type(p) == str:
        print (f'{p:.<30}', end =' ')
    else:
        print (f'R$ {p:.2f}')
'''
count = 0
for p in lista:
    if count % 2 == 0:
        print (f'{p:.<30}', end=' ')
    else: print (f'R$ {p:.2f}')
    count += 1
'''