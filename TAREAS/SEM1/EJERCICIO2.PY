#Escribe un programa que solicite al usuario un número entero y calcule su cuadrado y cubo
import math
num1 = int(input("Escribe un número entero: "))
potencia1= int(math.pow(num1,2))
potencia2= int(math.pow(num1,3))
print("El cuadrado del número es: ", potencia1)
print("El cubo del número es: ", potencia2)