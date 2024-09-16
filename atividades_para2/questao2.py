qnt = 0
pst = 0
for contador in range(8):
    numero = int (input(" Insira um numero :"))
    
    if numero < 0:
        qnt +=1
    elif numero > 0:
        pst += numero 
    
print(f" A quantidade de numeros negativos é {qnt} e a soma dos numeros positivos é {pst}")

