#Contador de mayusculas

import string

texto = input("Introduzca el texto: ")
mayusculas=0

for letra in texto:
    if letra in string.ascii_uppercase:
        mayusculas+=1

print("Las mayusculas son: {}".format(mayusculas))
