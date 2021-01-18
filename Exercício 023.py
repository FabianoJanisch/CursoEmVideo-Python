#Em forma de string
'''numero = str(input('Digite um número de 0 até 9999 '))
print ('Milhar: {}'.format(numero[0]))
print ('Centena: {}'.format(numero[1]))
print ('Dezena: {}'.format(numero[2]))
print ('Unidade: {}'.format(numero[3]))'''

#Em forma matemática
num = int(input('Digite aqui um número '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print (f'Analisando o número {num}')
print ('Unidade: {}'.format(u))
print ('Dezena: {}'.format(d))
print ('Centena: {}'.format (c)) 
print ('Milhar: {}'.format (m))
