objetos = ('Lápis','Borracha','caderno')
print(objetos[2]) # Começa a exibir o item na posição 1, ou seja segunda posição,uma vez que toda coleção começa na posição 0.

print(type(objetos))# irá mostrar o tipo da variável

print( objetos) # exibindo todos os itens de uma só vez

print("-"*50) 
for item in range(0,3):
    print(objetos[item], end=",") # exibindo todos os itens da tupla "de forma invidual"

# Exibindo todos os intens da tupla sem a função range
print("")
print("-"*50) 
for elementos in objetos:
    print(elementos) 

# Iremos tentar alterar o conteúdo da tupla

objetos[0] = "Caneta"