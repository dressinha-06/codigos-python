tA = 0
tAB = 0
media = 33.5
for i in range(2):
    float(input(f" Digite a temperatura {i + 1}° :"))

    if tA >= media: 
        tA += 1
    elif tAB < media:
        tAB += 1

print(f"Temperaturas acima ou iguais a {media}: {tA}, Temperatudas abaixo da {media}: {tAB} ")