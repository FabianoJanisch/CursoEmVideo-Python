r = 'S'
while r == 'S':
    sexo = input('Sexo [M/F]: ').upper().strip()
    if sexo == 'M' or sexo == 'F' or sexo == 'MASCULINO' or sexo == 'FEMININO':
        r = 's'
    else:
        print ('Dados inválidos, por favor digite novamente')
if sexo == 'M' or sexo == 'MASCULINO':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'

print (f'Sexo {sexo} cadastrado com sucesso')

