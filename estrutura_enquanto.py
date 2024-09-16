#1ª forma de ultilizar while - semelhante ao FOR

contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1 # é o mesmo que contador +=1

print("="*40)
#2ª forma de ultilizar enquanto - loop condicional normal
valor = 0

while valor >= 0:
    valor = int(input("Informe um valor qualquer(digite um valor negativo para terminar:)"))

    print(f"Você digitou {valor}")


while True:
    senha = input("informe a senha:")
    
    if senha == "123":
        print("parabéns, senha correta")
        break #informa o fim do loop
    else:
        print("senha incorreta, tente de novo")
