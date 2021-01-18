soma = 0
count = 0
countT = 0
for n in range(1, 7):
    num = int(input(f'Digite seu {n} número: '))
    countT = countT + 1
    if num % 2 == 0:
        soma = soma + num
        count = count + 1
if count == 0:
    count = 'nenhum'
print (f'Dos {countT} números {count} são pares, e a soma deles é {soma}')