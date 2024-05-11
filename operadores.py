#round (numero, decimales que quiero)
import math
num1 = int(input("Ingresa el número 1: "))
num2 = int(input("Ingresa el número 2: "))
suma = num1 + num2
resta = num1 - num2
multiplicación = num1*num2
división = num1 / num2
ecuacuión = (num1 - num2) * división
potencia = math.pow(num1,2)
residuo = num1%num2
print("La suma es: ",suma)
print("La resta es: ",resta)
print("El producto es: ",multiplicación)
print("La constante es : ",round(división,2))
print("El resultado es: ",round(ecuacuión,2))
print("El número 1 al cuadrado es: ",int(potencia))
print("El residuo es: ", residuo)