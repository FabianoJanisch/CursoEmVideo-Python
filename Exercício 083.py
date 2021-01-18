e = input('Digite uma expressão matemática: ')
cont = e.count ('(')
cont2 = e.count (')')
if cont == cont2:
    print ('Sua expressão está válida')
else:
    print('Sua expressão não está válida!')
 