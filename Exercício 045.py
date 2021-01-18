import random
import time

while True:
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = random.randint(0, 2)
    pessoa = int(input("[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura\n"))
    print ('-'*30)
    print (f'O computador escolheu {itens[computador]}')
    print (f'A pessoa escolheu {itens[pessoa]}')
    print ('-'*30)

    if computador == 0:             #Pedra 
        if pessoa == 0:
            print ('Empate')
        
        elif pessoa == 1:
            print ('Você venceu')

        elif pessoa == 2:
            print ('Você perdeu')
        
        else:
            print ('Erro')

    elif computador == 1:         #Papel
        if pessoa == 0:
            print ('Voce perdeu')
        
        elif pessoa == 1:
            print ('Empate')

        elif pessoa == 2:
            print ('Voce venceu')
        
        else:
            print ('Erro')

    elif computador == 2:        #Tesoura
        if pessoa == 0:
            print ('Você venceu')
        
        elif pessoa == 1:
            print ('Você perdeu')

        elif pessoa == 2:
            print ('Empate')
        
        else:
            print ('Erro')
    print ('-'*30)
    print ('\n')
