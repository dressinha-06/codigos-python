animais = ["Cachorro","Gato","Ovelha","Cobra"]
print(type(animais)) #Exibindo o tipo da variável

print( animais)

#Exibindo todos  os itens da lista
print("-")
for itens in animais:
    print(itens)

#1ª Etapa: Atualizar dados
print("-"*50)
animais[0] = "Coelho"
print(animais)

#2ª Etapa: Inserir dados
print("-"*50)
#Forma 1 - Usando append
animais.append("Cavalo") #Irá inserir um ite na final da lista 
print(animais)

#Forma 2 - Usando insert
animais.insert(1,"Pássaro") #O insert precisa de 2 valors, 1º será o índice que  deseja inserir o valo .
# O 2º é o conteúdo que eu quero inserir na lista
print(animais)

#3ª Etapa: Excluar dados
print("-"*50)
#Forma 1 - usado pop()
animais.pop() #Remove Últimos item da lista
print(animais)

#Forma 2 - usando pop() com índice
animais.pop(0) # Aqui iremos escolher qual índice da lista será excluído
print(animais)

#Forma 3 - Usando remove 
animais.remove("Ovelha") #Irá remover o itempela seu conreúdo
print(animais)
