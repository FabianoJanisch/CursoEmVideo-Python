n1 = int(input('Digite aqui seu primeiro número '))
n2 = int(input('Digite aqui seu segundo número '))
n3 = int(input('Digite aqui seu terceiro número '))

lista = [n1, n2, n3]
lista_crescente = sorted(lista)
'''print ('O maior valor digitado foi {}\nO menor valor digitado foi {}'.format(lista_crescente[-1], lista_crescente[0]))'''
print ('O maior valor digitado foi {}\nO menor valor digitado foi {}'.format(max(lista_crescente), min(lista_crescente)))
