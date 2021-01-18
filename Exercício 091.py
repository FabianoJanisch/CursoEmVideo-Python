from random import randint
import time
cont = 1
dados = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
for k, v in dados.items():
    print (f'{k} tirou {v}')
    time.sleep(0.8)
dadosorg = sorted(dados.items(), key=lambda x: x[1], reverse=True)
print (25*'-')
print ('Raking dos jogadores'.center(24).upper())
for k, v in dadosorg:
    print (f'{cont}° lugar: {k} com {v}')
    cont += 1
    time.sleep(0.9)
