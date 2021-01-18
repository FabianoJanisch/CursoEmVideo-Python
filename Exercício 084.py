pessoas = list()
dados = []
maiorp = menorp = 0
numero = n = n2 = 0
while True:
    dados.append(input('Nome: ').strip().capitalize())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])

    if numero == 0:
        maiorp = menorp = dados[1]
    else:
        if dados[1] > maiorp:
            maiorp =  dados[1]
        if dados[1] < menorp:
            menorp = dados[1]
    numero += 1
    dados.clear()
    while True:
        continuar = input('Você deseja cadastrar mais uma pessoa? [S/N] ').strip().upper()
        if not continuar or continuar not in 'SsNn':
            print ('Por favor, digite novamente. ')
        else:
            break
    if continuar in 'N':
        break

print (f'Foram cadastradas {len(pessoas)} pessoas')
print (f'O maior peso registrado foi de {maiorp}Kg dos nomes ', end = '')
for p in pessoas:
    if p[1] == maiorp:
        if n == 0:
            print (f'{p[0]}', end = '')
        elif n >= 1:
            print (f', {p[0]}', end = '')
        n += 1

print (f'\nO menor peso registrado foi de {menorp}Kg dos nomes ', end = '')
for p in pessoas:
    if p[1] == menorp:
        if n2 == 0:
            print (f'{p[0]}', end = '')
        elif n2 >= 1:
            print (f', {p[0]}', end = '')
        n2 += 1
