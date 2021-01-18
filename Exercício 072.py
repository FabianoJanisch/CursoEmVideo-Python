lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite seu número de 0 a 20: '))
    if n < 0 or n > 20:
        print ('Número incorreto. ', end ='')
    if 0 <= n <= 20:
        print (f'O número digitado foi {lista[n]}')
        continuar = input('Você deseja continuar? [S/N] ').upper().strip()
        if continuar == 'N':
            break
print ('Fim do programa :)')

