carrokm = float(input('Quantos km seu carro andou? '))
carrodia = float(input('Quantos dias o carro foi alugado? '))

valorkm = carrokm*0.15
valordia = carrodia*60

valor = valorkm + valordia
print (f'Seu valor é R${valor}')
