reta1 = float(input('Digite o tamanho da primeira reta '))
reta2 = float(input('Digite o tamanho da segunda reta '))
reta3 = float(input('Digite o tamanho da terceira reta '))

lista = [reta1, reta2, reta3]
lista_o = sorted(lista)
if lista_o[0] < lista_o[1] + lista_o[2] and lista_o[1] < lista_o[0] + lista_o[2] and lista_o[2] < lista_o [0] + lista_o[1]:
    print ('O triângulo existe')
else:
    print ('O triângulo NÃO existe')
