notas = []

while True:
    nota = float(input("Digite a nota do aluno (digite 0 para terminar): "))
    if nota == 0:
        break
    notas.append(nota)

media = sum(notas) / len(notas) if notas else 0

AM = sum(1 for nota in notas if nota > 7) # AM = Acima da Media

print("Quantidade de alunos com notas acima da média:", AM)