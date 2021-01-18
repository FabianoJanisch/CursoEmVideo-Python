futebol = ('São Paulo', 'Flamengo', 'Atlético-MG', 'Internacional', 'Grêmio', 'Palmeiras', 'Fluminense', 'Santos', 'Corinthians', 'Atlético-GO', 'Ceará SC', 'Athletico-PR', 'Bragantino', 'Fortaleza', 'Sport Recife', 'Bahia', 'Vasco da Gama', 'Botafogo', 'Coritiba', 'Goiás')


print (f'Os 5 primeiros colocadaos são {futebol[:5]}\n')
print (f'Os últimos 4 colocados da tabela são {futebol[-4:]}\n')
print (f'Os times em ordem alfabética é {sorted(futebol)}\n')
print ('O time da chapecoense não está na tabela de 2020, entretanto na tabela de 2019 está na posição de Coritiba que é {}'.format (futebol.index('Coritiba')+1))



#for f in futebol:
 #   print (f)