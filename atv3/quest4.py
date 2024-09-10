sal = int (input("Informe seu salário: "))

if sal <= 1900:
    print ("Você está insento do imposto de renda.")
if sal >= 1901 and sal <=2800:
    print (f"Seu imposto de renda é de 7,5%. Você deverá pagar R$ {sal*0.075}.")
if sal >= 2801  and sal <=3700:
    print (f"Seu imposto de renda é de 15%. Você deverá pagar R$ {sal*0.15}.")
if sal >= 3701:
    print (f"Seu imposto de renda é de 22,5%. Você deverá pagar R$ {sal*0.225}.")
