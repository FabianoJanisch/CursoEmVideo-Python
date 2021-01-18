peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura**2)

if imc < 18.5:
    print (f"Seu imc é {imc:.1f} e está abaixo do peso")
elif imc < 25:
    print (f"Seu imc é {imc:.1f} e está no peso ideal")
elif imc < 30:
    print (f"Seu imc é {imc:.1f} e está com sobrepeso")
elif imc < 40:
    print (f"Seu imc é {imc:.1f} e está com obesidade")
else:
    print (f"Seu imc é {imc:.1f} e está com obesidade mórbida")
