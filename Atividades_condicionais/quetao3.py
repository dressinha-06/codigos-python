a = int(input("Diga um valor: "))
b = int(input("Diga um valor novamente: "))

if a==b:
    c = (a+b)
    print(f"{c} é a soma de {a} e {b}")
else:
    c = (a*b)
    print(f"{c} é o produto de {a} e {b}")