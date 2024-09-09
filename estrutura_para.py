'''
Estes código é uma representação do que acontece 
na maioria das linguagens de programação

for(contador=1; contador<=5; contador++){

}
'''
# Primeira forma de operação do for
for contador in  range(1,10):
    print(contador)

print("_"*40) # Dessa forma vc consegue multiplicar o que está dentro das aspas
# Segunda forma de operação do for
for  contador in range(1,11,2): # O 3º parâmetro indica com os valores serão incrementados(alteração de valor)
    print(contador)

print("_"*40)
# Terceira forma de ultilizar o for
for  contador in range(10,0,-1):
    print(contador)

print("_"*40)
# A função end informa como os valores serão exibidos ao final, por padrão é dado um enter(\n)
for  contador in range(10,0,-1):
    print(contador, end=" ") 