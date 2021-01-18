'''numcatadj = float(input('Digite aqui o comprimento do cateto adjacente '))
numcatopo = float(input('Digite aqui o comprimento do cateto oposto '))
valor = (numcatadj**2 + numcatopo**2) **(1/2)
print (f'A soma desses valor forma o valor da hipotenusa {valor}')'''

import math
ca = float(input('Digite aqui o valor do cateto adjacente '))
co = float(input('Digite aqui o valor do cateto oposto '))
hi1 = (ca**2 + co**2)
hi = math.sqrt(hi1)
print ('O valor da hipotenusa é {:.2f}'.format (hi))
