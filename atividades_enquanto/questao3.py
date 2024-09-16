import random

numbersecret = random.randint(1,100)
print("Tente adivinha o numero secreto, você terá 5 tentativas")
tm = 5
t = 0
print(numbersecret)
while t < tm:

    dig = int(input(f"{t + 1}º tentativa, diga o numero!"))
    t+= 1
    if dig > numbersecret:
        print(f"O numero {dig} é maior do que o numero secreto")
    elif dig < numbersecret:
        print(f"O numero {dig} é menor do que o numero secreto")
    elif dig == numbersecret:
        print(f"você acertou !!! O numero secreto é {numbersecret}")
        break
    else:
        print(" pen, pen, pen, você perdeu, tente de novo")
