from datetime import date

ano = int(input("Ano de nascimento: "))

anoatual = date.today().year
idade = anoatual - ano

if idade <= 9:
    print (f"O atleta tem {idade} anos\nClassificação: Mirim")
elif idade > 9 and idade <= 14:
    print (f"O atleta tem {idade} anos\nClassificação: Infantil")
elif idade > 14 and idade <= 19:
    print(f"O atleta tem {idade} anos\nClassificação: Junior")
elif idade > 19 and idade <= 25:
    print (f"O atleta tem {idade} anos\nClassificação: Sênior")
elif idade > 25:
    print (f"O atleta tem {idade} anos\nClassificação: Master")
