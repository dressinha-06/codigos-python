v = float (input("Digite o valor da sua compra: "))
p = float (input("Digite a quantidades de parcelas (1 a 24): "))


if p > 12:
    print (f"O valor das parcelas são de R$ {v/p+6:.2f}. O valor total é: R$ {(((v/p+6)*p)*0.015) + ((v/p+6)*p):.2f}") #tirei 1,5% das parcelas somadas com 6
else:
    print(f"O valor das parcelas são de R$ {v/p}. O valor total é: {v}")