tupla = ('banana', 'morcego', 'ronaldo', 'cabeca grande', 'torta',
        'linguagem', 'ingles', 'pedala', 'tangerina', 'praticar')

for l in tupla:
    print (f'Na palavra {l} possui ', end ='')
    if 'a' in l:
        a = l.count('a')
        print (a*' a ', end ='')
    if 'e' in l:
        e = l.count('e')
        print (e*' e ', end ='')
    if 'i' in l:
        i = l.count('i')
        print (i*' i ', end ='')
    if 'o' in l:
        o = l.count('o')
        print (o*' o ', end ='')
    if 'u' in l:
        u = l.count('u')
        print (u*' u ', end= '')
    print ('\n')
