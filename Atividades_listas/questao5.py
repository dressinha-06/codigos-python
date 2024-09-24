import random
port = []

while True:
    lista = ["Cara", "Coroa"]
    sorteio = random.choice(lista)
    print(sorteio)  

    jogar_novamente = (input("Jogar novamente? (sim/não): "))
    port.append(sorteio) 
    if jogar_novamente == 'não':
        print( port)
        break




