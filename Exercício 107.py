from ex107 import moedas

n = int(input('Digite o valor: R$'))
print (f'A metade de {n} é {moedas.metade(n)}')
print (f'O dobro de {n} é {moedas.dobro(n)}')
print (f'Aumentando em 10%, temos {moedas.aumentar(n, 10)}')
print (f'Diminuindo em 10%, temos {moedas.diminuir(n, 10)}')
