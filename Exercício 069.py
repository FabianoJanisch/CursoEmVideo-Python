
i18 = sexo = f20 = 0
i = 0
continuar = True
while True:
    anula = True
    anula2 = True
    print (40*'-')
    centro = 'Cadastro de pessoas'
    print (centro.center(40))
    print (40*'-')
    while(anula):
        i = int(input('Idade: '))
        anula = False
    while(anula2):
        s = input('Sexo [M/F]: ').upper().strip()
        if s == 'M' or s == 'F':
            anula2 = False
    if i >= 18:
        i18 += 1
    if s == 'M':
        sexo += 1
    if i < 20 and s == 'F':
        f20 += 1

    while True:
        deseja = input('Você deseja continuar? [S/N]').upper().strip()
        if deseja == 'S':
            break
        if deseja == 'N':
            break
    if deseja == 'N':
        break

print (f'Pessoas cadastradas maior de 18 anos: {i18}\nHomens cadastrados: {sexo}\nMulheres cadastradas com menos de 20 anos: {f20}')
