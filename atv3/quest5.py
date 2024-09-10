h = int (input("Informe as horas você trabalhadas: "))
v = int (input("Informe o ganho por hora: ")) 

if h>40:
    print (f"O bônus do funcionário é de R$ {((h - 40)*v)*0.50}.")
else:
    print ("Sem bônus. O funcionário não possui horas extras.")