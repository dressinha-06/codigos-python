lista1 = input("Digite os números da primeira lista, separados por espaço: ")
l1 = [int(num) for num in lista1.split()]

lista2 = input("Digite os números da segunda lista, separados por espaço: ")
l2 = [int(num) for num in lista2.split()]

inter = sorted(set(l1) & set(l2))

print("Números comuns em ordem crescente:", inter)