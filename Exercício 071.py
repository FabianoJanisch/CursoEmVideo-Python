
cedula50 = cedula20 = cedula10 = cedula1 = 0
sacar = int(input('Qual valor você deseja sacar? R$'))
if sacar / 50 >= 1:
    cedula50 = sacar / 50
    cedula50 = round(cedula50 -0.5)
    sacar = sacar - cedula50*50
if sacar / 20 >= 1:
    cedula20 = sacar / 20
    cedula20 = round(cedula20 -0.5)
    sacar = sacar - cedula20*20
if sacar / 10 >= 1:
    cedula10 = sacar / 10
    cedula10 = round(cedula10 - 0.5)
    sacar = sacar - cedula10*10
if sacar >= 1:
    cedula1 = sacar / 1
    cedula1 = round(cedula1)
    sacar = sacar - cedula1*1
print (f'Possui {cedula50} cédulas de R$50')
print (f'Possui {cedula20} cédulas de R$20')
print (f'Possui {cedula10} cédulas de R$10')
print (f'Possui {cedula1} cédulas de R$1')
print (sacar) 


''' #usando while
sacar = int(input('Qual valor você deseja sacar? R$'))
valor = sacar
cedula = 50
totalc = 0
while True:
    if valor >= cedula:
        valor -= cedula
        totalc += 1
    else:
        if totalc > 0:
            print (f'Possui {totalc} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalc = 0
        if valor == 0:
            break
'''