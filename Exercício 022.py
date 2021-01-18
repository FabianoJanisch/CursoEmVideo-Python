nomec = str(input('Digite aqui seu nome completo ')).strip()
print ('O nome com todas as letras maiúsculas é: {}'.format(nomec.upper()))
print ('O nome com todas as letras minúsculas é: {}'.format(nomec.lower()))
print ('O número de letras que contém sem considerar espaços é: {}'.format (len(nomec) - nomec.count(' ')))
print ('A quantidade de letras que possui o primeiro nome é: {}'.format (len (nomec.split()[0])))

print ('Seu primeiro nome tem {}'.format (nomec.find(' ')))
