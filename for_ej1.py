#tabla de multiplicar
numero=int(input("Numero a multiplicar: "))

for n in range (1, 13):
#    if n % 2 == 0:
# para sacar multiplos de 2 y de acuerdo al numero que quieras se modifica el "2"
     print("{} * {} = {}".format(n, numero, n*numero))
