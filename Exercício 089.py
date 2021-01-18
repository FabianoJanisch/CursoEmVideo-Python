lista = []
temp = []
c = 0
while True:
    nome = input('Nome: ').strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    temp.append(nome)
    temp.append(nota1)
    temp.append(nota2)
    lista.append(temp[:])
    temp.clear()
    print (lista)
    while True:
        continuar = input('Quer adicionar mais notas? [S/N]] ').upper().strip()
        if not continuar in 'SN':
            print('Por favor, digite novamente')
        else:
            break
    mostrar = ' '
    if continuar == 'N':
        while True:
            print (50*'-')
            print ('N°      NOME                 MÉDIA')
            print (40*'_')
            for num, p in enumerate(lista, start=1):
                media = (lista[c][1] + lista[c][2]) / 2
                print (f'{num}   {lista[c][0]:^15}        {media:^10} ')
                c += 1
            while True:
                mostrar = int(input('Deseja mostrar notas de qual aluno? (999 to stop) ')) - 1
                if mostrar == 999-1:
                    break
                if mostrar <= len(lista):
                    print (f'As notas do {lista[mostrar][0]} são {lista[mostrar][1]} e {lista[mostrar][2]}')
                else:
                    print (f'Por favor, digite um número entre 1 e {len(lista)}')
            if mostrar == 999:
                break
    if mostrar == 999:
        break
print ('FIM :)')
