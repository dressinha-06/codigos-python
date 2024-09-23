import random


res = (input("Você deseja jogar? "))

while res == "sim":
    print("Vamos jogar pedra, papel e tesoura!!!")

    pirupi = random.randint(1,3)
    print(pirupi)
    jog = input("pedra, papel ou tesoura? ")

    if pirupi == 1 and jog == "pedra":
        print("DEU EMPATE!!")

    if pirupi == 2 and jog == "papel": 
        print("DEU EMPATE!!")

    if pirupi == 3 and jog == "tesoura":
        print("DEU EMPATE!!")

    if pirupi == 1 and jog == "papel":
        print("Papel ganha Pedra")

    if pirupi == 1 and jog == "tesoura":
        print("Pedra ganha Tesoura")

    if pirupi == 2 and jog == "tesoura":
        print("Tesoura ganha Papel")

    res = (input("Você deseja jogar novamente? "))
    if res == "não":
        break
