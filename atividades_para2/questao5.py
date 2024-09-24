n = int(input("Quantos números você deseja inserir?"))

valores = []
for i in range(n):
    numero = int(input(f"Digite a {i + 1}° número: "))
    valores.append(numero)

maiorV = max(valores)
posicaoMV = valores.index(maiorV) + 1
print(f"O maior valor é {maiorV} e foi inserido na {posicaoMV}ª posição.")