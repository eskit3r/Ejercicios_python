lista = []
input_usuario = None

while input_usuario != "Q":
    input_usuario = input("¿Que desea comprar?(Q para salir):")
    if input_usuario == "Q":
        pass
    elif input_usuario in lista:
        print("{} ya esta en la lista".format(input_usuario))
    else:
        if input ("¿Seguro que quieres añadir {} a la lista de compras? [S/N]:".format(input_usuario)) == "S":
            lista.append(input_usuario)

print("La lista de compras son:{}".format(lista))
