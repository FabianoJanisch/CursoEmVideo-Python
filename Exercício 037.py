n = int(input('Digite aqui um número inteiro '))
opção = int(input('Você deseja converter para:\n[ 1 ] Binário\n[ 2 ] Octal\n[ 3 ] Hexadecimal:\n'))
if opção == 1:
    print ("O seu número {} convertido para binário é {}".format (n, bin(n)[2:]))
elif opção == 2:
    print ("O seu número {} convertido para octal é {}".format (n, oct(n)[2:])) 
elif opção == 3:
    print ("O seu número {} convertido para hexadecimal é {}".format (n, hex(n)[2:]))
else:
    print ('Por favor, digite um número de 1 a 3')
