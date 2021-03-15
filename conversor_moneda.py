import time
print("Hola, quiero cambiar mis libras a euros")
time.sleep(2)
tc=1.17
print("Buenos dias, el tipo de cambio es " +str(tc))
time.sleep(2)

b=float(input("Ingrese la cantidad de libras a cambiar:"))

c=b*tc

print("Su dinero cambiado seria " +str(c)+ " euros")