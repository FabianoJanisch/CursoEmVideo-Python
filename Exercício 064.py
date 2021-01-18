
parar = True
cont = 0
soma = 0
while(parar):
    n = int(input('Digite um número (999 to stop): '))
    if n != 999:
        soma += n
        cont += 1
    if n == 999:
        parar = False
print (f'Você digitou {cont} números e sua soma foi {soma}')