dic = {}
gols = []
c = 0
dic['nome'] = input('Nome do Jogador: ').capitalize().strip()
partidas = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
for p in range (1, partidas+1):
    gols.append(int(input(f'Quantos gols na partida {p}? ')))
dic['gols'] = gols
dic['total'] = sum(gols)
print (30*'-')
print (dic)
print (30*'-')
for k, v in dic.items():
    print (f'{k} tem valor {v}.')
print (30*'-')
print (f'O jogador {dic["nome"]} jogou {partidas} partidas')
for p in range (1, partidas+1):
    print (f'Na partida {p}, fez {dic["gols"][c]} gols'.rjust(27))
    c += 1
print (f'No total, foram {dic["total"]} gols')
