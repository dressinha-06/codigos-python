ano = int (input("Digite um ano do calendário: "))

if ano % 400 == 0 or ano % 4 == 0 or ano % 100 == 1:
    print (f"{ano} é um ano bissexto.")
else:
    print (f"{ano} não é um ano bissexto.")
