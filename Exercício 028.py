import random

lista = ['0', '1', '2', '3', '4', '5']
computador = int(random.choice(lista))

pessoa = int(input('Digite aqui um número de 0 a 5: '))
print (f'O número escolhido do computador foi {computador}')
if pessoa == computador:
    print ('Parabéns, você venceu!')
else:
    print ('Infelizmente você perdeu')

