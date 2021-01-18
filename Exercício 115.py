from ex115.interface import *
from ex115.arquivo import *
from time import sleep

arq = 'cadastro.txt'

if not arquivoE(arq):
    criarArquivo(arq)

while True:
    início()
    opções = opção('\033[33mSua opção:\033[m ')
    if opções == 1:
        print (30*'-')
        print ('Pessoas cadastradas'.center(30))
        print (30*'-')
        arquivo = open('cadastro.txt', 'rt')
        for pessoas in arquivo:
            dado = pessoas.split(';')
            dado[1] = dado[1].replace('\n', '')
            print (f'{dado[0]:<15}    {dado[1]:>5} anos')
        arquivo.close()
    elif opções == 2:
        print (30*'-')
        print ('Novo cadastro'.center(30))
        print (30*'-')
        arquivo = open('cadastro.txt', 'a')
        nome = input('Nome: ').capitalize().strip()
        idade = leiaInt('Idade: ')
        arquivo.write(f'{nome};{str(idade)}\n')
        print (f'{nome} de {idade} anos adicionado ao sistema')
        arquivo.close()
    elif opções == 3:
        print ('Fim do programa! ')
        break
    else:
        print ('\033[31mPor favor, digite um número de 1 a 3\033[m')
    sleep(1)