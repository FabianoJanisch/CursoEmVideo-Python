nomec = str(input('Digite o nome da sua cidade: ')).strip().lower()
bobo = nomec.split()
existe = ('santo' in bobo[0])
print (f'Existe o nome santo na sua cidade: {existe}')
