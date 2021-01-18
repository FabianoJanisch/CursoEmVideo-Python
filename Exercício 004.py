teclado = input('Digite aqui alguma coisa: ')


print ('O tipo primitivo é', type(teclado))
print ('Tem somente espaços?', teclado.isspace())
print ('Tem somente números?', teclado.isnumeric())
print ('É alfanumérico (tem letra ou número)?', teclado.isalnum())
print ('Tem somente letras?', teclado.isalpha())
print ('Tem somente letras minúsculas?', teclado.islower())
print ('Tem somente letras maiúsculas? ', teclado.isupper())
print ('Está capitalizada (No começo maiúsculo e resto minúsculo)?', teclado.istitle())

print ('------------------teste----------------------')
print (f'João viadão {teclado.isnumeric()}')

print ('João bobão {}'.format (teclado.isnumeric()))

print ('{} É uma letra? {}'.format (teclado, teclado.isalpha()))

print (f'João é cabaço {teclado.isalnum()}')
