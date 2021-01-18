def fatorial(num, show=False):
    '''
    -- Calcula o fatorial de um número.
    :param num: número a ser calculado.
    :param show: Mostrar ou não a conta (Opcional).
    :param return: O valor do fatorial de um número num. 
    '''
    f = 1
    for n in range(num, 0, -1):
        f = f*n
        if show == True:
            if n == 1:
                print (n, end = ' ')
                print (f'= {f}')
            else:
                print (n, end = ' x ')
    if show == False:
        return print (f)


fatorial(5)