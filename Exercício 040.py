nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
m = (nota1 + nota2)/2 
if m < 5:
    print (f"Sua média foi {m} e está REPROVADO!")
elif m >= 5 and m < 7:
    print (f"Sua média foi {m} e está em recuperação")
elif m >= 7:
    print (f"Sua média foi {m} e está aprovado!")
