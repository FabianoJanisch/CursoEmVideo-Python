import time
dic = dict()
dic['nome'] = input('Nome: ').capitalize().strip()
ano = int(input('Ano de nascimento: '))
dic['idade'] = time.gmtime()[0] - ano
dic['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
if dic['carteira'] != 0:
    dic['contratação'] = int(input('Ano de contratação: '))
    dic['salário'] = float(input('Salário: R$'))
    dic['aposentadoria'] = 35 + (dic['contratação'] - ano)
print (25*'-')
for k, v in dic.items():
    if 'idade' in k or 'carteira' in k or 'contratação' in k:
        l = 'A'
    else:
        l = 'O'
    print (f'{l} {k} tem valor {v}')