import time
ano = time.gmtime()[0]
maior = 0
menor = 0
for n in range (1, 7+1):
    nas = int(input(f'Qual ano a {n}° pessoa nasceu? '))
    nas2 = ano - nas
    if nas2 >= 21:
        maior = maior + 1
    elif nas2 <21:
        menor = menor + 1
print ('São no total {} pessoas maiores de idade e {} pessoas menores de idade'.format (maior, menor))
