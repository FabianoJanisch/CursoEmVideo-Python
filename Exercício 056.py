idadef = 0
idadem = []
nomev = ''
maisv = 0
media = 0
for p in range (1, 5):
    print (10*'-', f'{p}° pessoa', 10*'-')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    media = idade + media
    #[]
    if sexo == 'M':
        idadem = idadem + [idade]
        idademv = sorted(idadem)
    if p == 1 and sexo == 'M':
        maisv = idade
        nomev = nome
    if sexo == 'M' and idade > maisv:
        maisv = idade
        nomev = nome
    if sexo == 'F':
        if idade < 20:
            idadef = idadef + 1



print (f'A média de idade do grupo é {media/4}')
print (f'O nome do homem mais velho é {nomev} e tem {idademv[-1]} anos')
print (f'São no total {idadef} mulheres que tem menos de 20 anos')

