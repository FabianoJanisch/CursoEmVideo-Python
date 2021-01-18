def leiaDinheiro(msg):
    validar = False
    while not validar:
        numero = str(input(msg)).strip().replace(',', '.')
        if numero.isalpha() or numero == '':
            print ('\33[31mErro! Digite um preço válido\33[m')
        else:
            validar = True
            return float(numero)
