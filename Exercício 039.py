from datetime import date

ano = int(input("Ano de nascimento: "))
anoatual = date.today().year
idade = anoatual - ano
jafoi =  ano + 18
jafoi2 = anoatual - jafoi
aindavai = 18 - idade
if idade == 18:
    print ("Esse ano é o seu alistamento!")
if idade > 18:
    print (f"Já se passou {jafoi2} anos de seu alistamento e foi em {jafoi}")
if idade < 18:
    print (f"Seu alistamento será em {jafoi} e faltam {aindavai} anos")
