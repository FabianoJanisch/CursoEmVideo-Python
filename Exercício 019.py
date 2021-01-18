from random import choice
nome1 = input('Digite o nome do seu primeiro aluno: ')
nome2 = input('Digite o nome do seu segundo aluno: ')
nome3 = input('Digite o nome do seu terceiro aluno: ')
nome4 = input('DIgite o nome do seu quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
sorteio = choice(lista)
print (f'O aluno escolhido foi {sorteio}')
