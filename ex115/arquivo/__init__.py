def arquivoE(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print ('Houve um erro ao criar o arquivo')
    else:
        print (f'Arquivo {nome} criado com sucesso! ')


