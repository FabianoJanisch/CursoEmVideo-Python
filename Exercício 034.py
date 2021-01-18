salario = float(input('Qual é o seu salário? '))
if salario <= 1250:
    print ('Seu novo salário é R${:.2f}'.format (salario*1.15))
if salario > 1250:
    print ('Seu novo salário é R${:.2f}'.format (salario*1.10))

