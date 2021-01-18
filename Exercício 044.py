valor = float(input("Valor do produto: R$"))
forma = int(input('De que forma você deseja pagar?\n[ 1 ] À vista dinheiro/cheque\n[ 2 ] À vista cartão\n[ 3 ] Cartão parcelado\n'))
if forma == 1:
    nv = valor - (valor*0.10)
    print (f'Sua compra foi de R${valor:.2f} e com o desconto vai sair R${nv:.2f}')
elif forma == 2:
    nv = valor - (valor * 5 / 100)
    print (f'Sua compra foi de R${valor:.2f} e com o desconto vai sair R${nv:.2f}')
elif forma == 3:
    parcelado = int(input('\n[ 1 ] Até duas vezes no cartão\n[ 2 ] 3x ou mais no cartão\n'))
    if parcelado == 1:
        print (f'Sua compra foi de R${valor:.2f} e não há desconto')
    elif parcelado == 2:
        nv = valor + (valor * 20 /100)
        print (f'Sua compra foi de R${valor:.2f} e com os juros vai sair R${nv:.2f}')
