vcbruto = float(input("qual valor da conta? "))
gogo = float(input("Digite o percentual da gorjeta? "))

print(f" O valor da sua conta é {vcbruto} e o percentual da gorjeta é de {vcbruto*(gogo/100)}")
print("-"*50)
print(f" O valor da conta a pagar é  {vcbruto+(vcbruto*(gogo/100))} ")
