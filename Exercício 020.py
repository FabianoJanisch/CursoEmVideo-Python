'''import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista1 = [n1, n2, n3, n4]
random.shuffle(lista1)

print (lista1)'''

import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = random.sample([n1, n2, n3 , n4], k=3)
print (f'A lista de 4 pesssoas é{lista}')

lista2 = random.sample((lista), k=1)
print (f'A lista de 1 pessoa sorteda da lista sorteda é {lista2}')

