contadorm18 = 0

for i in range(5):
    idade = int(input(f"Digite a iade da pessoa {i + 1}: "))
    if idade >= 18:
        contadorm18 += 1
    print(f"A quantidade de pessoas com 18 anos  ou mais : {contadorm18}")