prdt = float(input("informe qual o valor do produto: \n"))
 
a = print("1-pix, dinheiro ou debito, recebe 15% de deconto")
b = print("2-Á vista no cartão de crédito 10% de desconto")

pag = (input("Informe a forma de pagamento: \n"))

if pag =="pix" or "dinheiro" or "debito":
    pg = (prdt*15)/100
    pf = pg+prdt

    print(f" o valor a ser pago é {pf}")

    # pc = (prdt*15)/100
    # pt = pag+pc
    # print(f"o valor a ser pago é{pt}")

    # c = print("3-Em duas vezes, preço normal sem juros")
    # d = print("4-Em três vezes normal mais juros de 10%")

    