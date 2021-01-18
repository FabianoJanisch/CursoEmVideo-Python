dic = dict()
dic['nome'] = input('Nome: ').capitalize().strip()
dic['média'] = float(input(f'Média de {dic["nome"]}: '))
print ()
if dic['média'] >= 7:
    dic['situação'] = 'Aprovado'
elif dic['média'] < 7 and dic['média'] >= 5:
    dic['situação'] = 'Recuperação'
else:
    dic['situação'] = 'Reprovado'
for k, v in dic.items():
    if 'média' in k or 'situação' in k:
        l = 'A'
    else:
        l = 'O'
    print (f'{l} {k} é {v}')
