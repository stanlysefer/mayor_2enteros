#programa para verificar cuál de dos números enteros es el mayor
print("-------------------------------------")
print("----------- MAYOR 2 ENTEROS----------")
print("-------------------------------------")

#input
x = int(input("Digite el valor de x: "))
y = int(input("digite el valor de y: "))

#processing
if x == y:
    #output
    print("los numeros son iguales...")
else:
    if x > y:
        mayor = x
    else:
         mayor = y
#output
print("El mayor entre " + str(x) + " y " + str(y) + " es " + str( mayor ))
