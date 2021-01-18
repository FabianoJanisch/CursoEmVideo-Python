velocidade = int(input('Escreva a velocidade do seu carro em km/h '))
if (velocidade) >80:
    multa = (velocidade - 80 ) * 7
    print (f'O valor da sua multa é R${multa} ')
else:
    print ('Parabens, você está no limite de velocidade')
