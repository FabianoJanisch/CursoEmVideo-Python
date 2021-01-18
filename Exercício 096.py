def área(l, c):
    a = l*c
    print (f'A área do seu terreno {l}x{c} = {a}m²')


print (30*'-')
print ('Calculador da área'.center(30))
print (30*'-')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)