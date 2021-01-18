continuar = True
soma = 0
cont = 0
maior = menor = 0
while(continuar):
    if(continuar):
        n2 = int(input('Digite um numero: '))
        soma += n2
        cont += 1
    continuar = input('Quer continuar? [S/N]: ').upper().strip()
    if continuar == 'N':
        continuar = False
    if cont == 1:
        maior = menor = n2
    else:
        if n2 > maior:
            maior = n2
        if n2 < menor:
            menor = n2
print (f'Foi digitado {cont} números e a média foi {soma/cont}\nO maior número é o {maior} e o menor foi {menor}')
 