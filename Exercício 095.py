dic = {}
gols = []
pessoas = []
c = 0
while True:
    dic['nome'] = input('Nome do Jogador: ').capitalize().strip()
    partidas = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
    for p in range (1, partidas+1):
        gols.append(int(input(f'Quantos gols na partida {p}? ')))
    dic['gols'] = gols[:]
    dic['total'] = sum(gols)
    pessoas.append(dic.copy())
    gols.clear()
    while True:
        continuar = input('Deseja continuar? [S/N] ').upper().strip()
        if continuar in 'SN':
            break
        else:
            print ('Por favor, digite somente S ou N')
    if 'N' in continuar:
        break
print (pessoas)
print (40*'-')
print (f'N°       {"Nome":^7}               {"Gols":^15}        {"Total":^27}')
for n, j in enumerate(pessoas, start=1):
    print (f'{n}        {str(j["nome"]):^7}             {str(j["gols"]):^15}          {str(j["total"]):^27} ')
print (40*'-')
while True:
    mostrar = int(input('Deseja mostrar os dados de qual jogador? (999 para parar) ')) - 1
    if mostrar == 999-1:
        break
    if mostrar >= len(pessoas) or mostrar <= -1:
                print(f'Por favor, digite um número entre 1 e {len(pessoas)}')
    else:
        print (f'\nLevantamento do jogador {pessoas[mostrar]["nome"]}')
        for n, j in enumerate(pessoas[mostrar]['gols']):
            print (f'   No jogo {n+1} fez {j} gols')
        print (f'   Foi um total de {pessoas[mostrar]["total"]} gols')
print ('Fim do programa! ')
