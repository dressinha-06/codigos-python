i = int (input("Digite sua idade: "))

if i <= 12:
    print (f"Você é uma criança.")
if i > 12 and i <=18:
    print (f"Você é um adolescente.")
if i > 18 and i <=60:
    print (f"Você é um adulto.")
if i > 60:
    print (f"Você é um idoso.")