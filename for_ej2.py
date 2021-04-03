lista_numeros=[]

numero_introducido=int(input("Introduzca el numero: "))
lista_numeros.append(numero_introducido)

while input("¿Desea introducir mas numeros? [S/N]: ")=="S":
    numero_introducido=int(input("Introduzca el numero: "))
    lista_numeros.append(numero_introducido)

print("Los numeros de la lista son: {}".format(lista_numeros))