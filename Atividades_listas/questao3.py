eventos = ["Reunião com a equipe",
           "Almoço com cliente",
           "Consulta médica"
           ]

def exibir_eventos():
    print("Eventos agendados:\n")
    for evento in eventos:
        print(f"{evento}")
    print()

while True:
    exibir_eventos()
    print("Menu de Gerenciamento de Eventos")
    print("1. Adicionar um novo evento")
    print("2. Remover um evento")
    print("3. Sair")
    
    opcao = input("Escolha uma opção (1-3): ")
    
    if opcao == "1":
        novo_evento = input("Digite o nome do novo evento: ")
        eventos.append(novo_evento)
    elif opcao == "2":
        posicao = int(input("Qual a posição do evento? ")) - 1
        if 0 <= posicao < len(eventos):
            eventos.pop(posicao)
        else:
            print("Posição inválida.")
    elif opcao == "3":
        break
    else:
        print("Opção inválida.")

print("Eventos finais:")
exibir_eventos()
