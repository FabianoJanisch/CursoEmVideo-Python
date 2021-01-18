import random

v = False
tots = 0
computador = random.randint(1,10)
while not v:
    pessoa = int(input('Digite um número de 0 a 10: '))
    if pessoa == computador:
        print (f'Parabéns, você venceu! O número que o computador escolheu foi {computador}')
        print (f'Foram necessárias \033[34m{tots} \033[0mtentativas necessárias para você vencer')
        v = True
    else:
        tots += 1
        print (f'Infelizmente você perdeu, tente novamente')
        if computador > pessoa:
            print (f'O número do computador é \033[33mmaior\033[0m!')
        if computador < pessoa:
            print (f'O número do computador é \033[33mmenor\033[0m!')

