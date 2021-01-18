c = ('\033[m',           # 0 Sem cores
     '\033[0;30;41m',    # 1 vermelho
     '\033[0;30;42m',    # 2 verde
     '\033[0;30;43m',    # 3 amarelo
     '\033[0;30;44m',    # 4 azul
     '\033[0;30;45m',    # 5 roxo
     '\033[7;30m'        # 6 branco
     )
 

def comando(com):
    titulo(f'Acessando o manual do comando \'{ajuda}\'', 4)
    print (c[6], end ='')
    help(com)
    print (c[0], end ='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print (tam*'-')
    print (f'  {msg}')
    print (tam*'-' )
    print (c[0], end ='')

 
ajuda = ''
while True:
    titulo('Manual de ajuda Python', 2)
    print (c[0])
    ajuda = input('Biblioteca ou função: ')
    if ajuda.upper() == 'FIM':
        break
    else:
        comando(ajuda)
titulo('Fim!', 1)
