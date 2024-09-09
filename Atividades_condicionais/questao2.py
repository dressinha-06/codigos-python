nome = (input("Diga seu nome: "))
sexo = (input("Diga seu seu sexo:"))
estadocil = (input("Diga seu estado civil: "))

if sexo=="Feminino" and estadocil=="casada":
    anos = int(input("Informe quantos anos de casada: "))
    print(f"{nome} casada a {anos} anos")

else:
    print(f" Obrigada {nome}, ate a proxima")  
