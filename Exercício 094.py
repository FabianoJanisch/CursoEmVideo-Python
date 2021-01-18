pessoas = []
ump = {}
tidade = 0
while True:
    ump['nome'] = input('Nome: ').capitalize().strip()
    while True:
        ump['sexo'] = input('Sexo [M/F]: ').upper().strip()[0]
        if ump['sexo'] in 'MF':
            break
        print('Por favor, digite somente M ou F')
    ump['idade'] = int(input('Idade: '))
    tidade += ump['idade']
    pessoas.append(ump.copy())
    while True:
        continuar = input('Deseja continuar [S/N]: ').upper().strip()
        if 'N' in continuar:
            break
        elif 'S' in continuar:
            break
        else:
            print ('Por favor, digite somente S ou N')
    if 'N' in continuar:
        break
média = tidade/len(pessoas)
print (f'Foram cadastradas {len(pessoas)} pessoas')
print (f'A média de idade do grupo é {média:.2f}')
print (f'A lista somente com mulheres é ', end = '')
for f in pessoas:
    if 'F' in f['sexo']:
        print(f'{f["nome"]} ', end = '')
print ()
print (f'A lista com pessoas acima da média de idade é ', end = '')
for m in pessoas:
    if m['idade'] >= média:
        print (f'{m["nome"]} ', end = '')
     