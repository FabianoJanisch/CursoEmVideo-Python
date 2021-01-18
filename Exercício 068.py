import random
print (40*'-')
centro = 'Jogo Par ou Ímpar'
print (centro.center(40))
print (40*'-')
soma = cont = 0
while True:
    n = int(input('Digite um número: '))
    escolha = input('Você escolhe \33[33mpar\33[m ou \33[33mímpar\33[m? [P/I] ').upper().strip()[0]
    while escolha not in 'PI' :
        escolha = input('Por favor, digite novamente: ').upper().strip()
        if escolha == 'I' or escolha == 'P':
            break
    print (40*'-')
    computador = random.randint(1, 10)
    soma = n + computador
    parimpar = soma % 2
    if parimpar == 0 and escolha == 'P':
        venceu = 'venceu'
        cont += 1
    elif parimpar == 1 and escolha == 'I':
        venceu = 'venceu'
        cont += 1
    else:
        venceu = 'perdeu'
    if parimpar == 0 or parimpar == 1:
        if escolha == 'P':
            escolha = 'par'
            print (f'Você jogou {n} e o computador {computador}, a soma foi {soma}.\nVocê escolheu {escolha} e \33[34m{venceu}\33[m!')
        if escolha == 'I':
            escolha = 'impar'
            print (f'Você jogou {n} e o computador {computador}, a soma foi {soma}.\nVocê escolheu {escolha} e \33[34m{venceu}\33[m!')
        if venceu == 'perdeu':
            break
print(f'Você venceu {cont} vezes')
    
