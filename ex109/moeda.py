
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
    print (f'Preço analisado: {moeda(preço):^14}')
    print (f'Metade do preço: {moeda(metade(preço)):^14}')
    print (f'Dobro do preço: {moeda(dobro(preço)):^14}')
    print (f'Aumento de {aum}%: {moeda(aumentar(preço, aum)):^14}')
    print (f'Diminuição de {dim}%: {moeda(diminuir(preço, dim)):^14}')
    print (30*'-')
