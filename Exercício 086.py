matriz = [[], [], []]
cont = c = c2 = 0
nmatriz1 = nmatriz2 = 0
while cont < 9:
    n = int(input(f'Digite um número para [{nmatriz1}, {nmatriz2}]:'))
    matriz[c].append(n)
    c2 += 1
    if c2 == 3:
        c +=1
        c2 = 0
    cont += 1
    nmatriz2 +=1
    if nmatriz2 == 3:
        nmatriz2 = 0
        nmatriz1 +=1
print (f"""[ {matriz[0][0]:^3} ] [ {matriz[0][1]:^3} ] [ {matriz[0][2]:^3} ]
[ {matriz[1][0]:^3} ] [ {matriz[1][1]:^3} ] [ {matriz[1][2]:^3} ]
[ {matriz[2][0]:^3} ] [ {matriz[2][1]:^3} ] [ {matriz[2][2]:^3} ] """)

'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print ()
for l in range(0, 3):
    for c in range(0, 3):
        print (f'[{matriz[l][c]:^5}]', end ='')
    print ()
'''