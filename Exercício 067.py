
while True:
    print (40*'-')
    n = int(input('Você deseja ver a tabuada de qual número? '))
    print (40*'-')
    if n < 0:
        break
    for t in range (1, 11):
        print (f'{n} x {t} = {n*t}')
print ('Fim do programa')
