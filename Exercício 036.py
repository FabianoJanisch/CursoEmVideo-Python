casa = float(input('Qual o valor da casa? '))
salário = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você deseja pagar? '))

meses = anos*12
prestação = casa/meses

if prestação > salário * 30 / 100:
    print ('Empréstimo NEGADO!')
else:
     print ('Empréstimo aceito')







print ('Para pagar a sua casa de R${} em {} anos a prestação será de R${:.2f} sendo seu salário de R${}'.format (casa, anos, prestação, salário))