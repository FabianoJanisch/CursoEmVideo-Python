frase = str(input('Digite aqui sua frase: ')).strip().lower()
print ('Sua frase contém a palavra A: {} vezes'.format(frase.count('a')))
print ('A posição que aparece pela primeira vez a letra A é: {}'.format((frase.find('a')+1)))
print ('A posição que aparece pela ultima vez é: {}'.format(frase.rfind('a')+1))

