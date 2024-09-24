import random
chances = 3
print("-"*155)
fruta = [ 'Maçã', 'Banana', 'Laranja', 'Morango', 'Uva', 'Abacaxi', 'Kiwi', 'Manga','Pera', 'Melancia', 'Framboesa', 'Tanja', 'Carambola', 'Figo', 'Amora' ]
print(fruta)

random.shuffle(fruta)

print("\nVamos jogar? Nesse jogo você terá que acertar em que posição a palavra dada se encontra. As posições são de 0 a 14, e você terá três chances para acertar.")
print("-"*155)

sorteada = random.choice(fruta)
posicao = fruta.index (sorteada)


while chances > 0:
    pose = input(f"Em qual posição a palavra '{sorteada}' se encontra? \n")

    pose = int(pose)  # Assume que a entrada é válida para fins de simplicidade

    if posicao == pose:
        print("Parabéns, você acertou!")
        break  # Sai do loop se o usuário acertar
    else:
        chances -= 1  # Decrementa as chances
        print(f"Você errou! Chances restantes: {chances}")
if chances == 0:
    print(f"\nVocê esgotou suas chances! A palavra '{sorteada}' estava na posição {posicao}.\n")
print (fruta)