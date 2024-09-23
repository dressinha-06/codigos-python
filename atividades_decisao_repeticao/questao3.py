import time

segun = int(input(" Quantos segundos você deseja: "))

for parapapu in range(segun, -1, -1):
    print(parapapu)
    time.sleep(1)

print("Tempo esgotado!")
