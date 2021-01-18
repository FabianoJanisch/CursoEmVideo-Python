
def dobro(a = 0):
    dobro = a*2
    return dobro


def metade(a = 0):
    metade = a/2
    return metade


def aumentar(a = 0, porc = 0):
    aumentar = a + (a*porc/100)
    return aumentar


def diminuir(a = 0, porc = 0):
    diminuir = a - (a*porc/100)
    return diminuir

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
