par = coluna3 = linha2 = cont = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            coluna3 += matriz[l][c]
        if l == 1:
            if cont == 0:
                linha2 = matriz[l][c]
                cont += 1
            if matriz[l][c] > linha2:
                linha2 = matriz[l][c]
print ()
for l in range(0, 3):
    for c in range(0, 3):
        print (f'[{matriz[l][c]:^5}]', end ='')
    print ()
print (f'\nA soma dos valores pares é {par}')
print (f'A soma dos valores da terceira coluna é {coluna3}')
print (f'A o maior valor da segunda linha é {max(matriz[1])}')
