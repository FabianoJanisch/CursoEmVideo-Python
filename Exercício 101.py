def voto(ano):
    import datetime
    idade = datetime.date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos, NÃO vota!'
    elif idade == 16 or idade == 17 or idade >= 65:
        return f'Com {idade} anos, o voto NÃO é obrigatório!'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos, o voto é OBRIGATÓRIO!'
ano = int(input('Ano de nascimento: ')) 
print (voto(ano))