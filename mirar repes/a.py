file = open("../Inicializador/list.txt", "r")
lineas = file.readlines()
for item in lineas:
    aux = 0
    for item2 in lineas:
        if(item==item2):
            aux = aux + 1
    if aux>1:
        print(item + "   " + str(aux))
print("a")
