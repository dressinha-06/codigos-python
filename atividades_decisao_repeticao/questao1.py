print("ciclismo, corrida, caminhada")
print("-"*50)
ativ = (input("Qual execicio fisico você praticou? "))
temp = int(input("Por quanto tempo você praticou o execicio fisico? "))

if ativ == "caminhada":
    caminhada = temp*5
    print(f"Você gastou {caminhada} calorias ")
    
elif "corrida":
    corrida = temp*10
    print(f"Você gastou {corrida} calorias ")

elif "ciclismo":
    ciclismo = temp*8
    print(f"Você gastou {ciclismo} calorias ")


