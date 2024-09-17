list = []

while True:
    va = int(input("insira um numero: "))
    if va < 0:
        break
    else:
        list.append(va)
print(list)

for cont in list:
     if cont% 2 == 0:
         list.remove(cont)
print(list)