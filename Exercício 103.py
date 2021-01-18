def ficha(n='DESCONHECIDO', g=0):
    if gols == '':
        g = 0
    print (f'O jogador {n} fez {g} gol(s) no campeonato')

nome = input('Nome do jogador: ').strip().capitalize()
gols = input('Número de gols: ')
if nome == '':
    ficha(g=gols)
else:
    ficha(nome, gols)

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
