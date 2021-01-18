
def dobro(a = 0, format=False):
    dobro = a*2
    return dobro if format is False else moeda(dobro)


def metade(a = 0, format=False):
    metade = a/2
    return metade if format is False else moeda(metade)


def aumentar(a = 0, porc = 0, format=False):
    aumentar = a + (a*porc/100)
    return aumentar if format is False else moeda(aumentar)


def diminuir(a = 0, porc = 0, format=False):
    diminuir = a - (a*porc/100)
    return diminuir if not format else moeda(diminuir)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço, aum, dim):
    print (30*'-')
    print ('Resumo dos valores'.center(30))
    print (30*'-')
    print (f'Preço analisado: \t{moeda(preço)}')
    print (f'Metade do preço: \t{metade(preço, True)}')
    print (f'Dobro do preço: \t{dobro(preço, True)}')
    print (f'Aumento de {aum}%: \t{aumentar(preço, aum, True)}')
    print (f'Diminuição de {dim}%: \t{diminuir(preço, dim, True)}')
    print (30*'-')
