#solicitud de 2 números y que muestre sum,resta,multp,div,div entera,residuo
import math
num1 = int(input("Ingresa el número 1: "))
num2 = int(input("Ingresa el número 2: "))
suma = num1 + num2
resta = num1 - num2
multiplicación = num1*num2
división = num1 / num2
residuo = num1%num2
print("La suma es: ",suma)
print("La resta es: ",resta)
print("El producto es: ",multiplicación)
print("El cociente es: ",división)
print("El cociente entero es: ",round(división,0))
print("El residuo es: ",residuo)