#Escribe un programa que solicite al usuario un número entero y calcule si es divisible por 3 y por 5.
num1 = int(input("Escribe un número entero: "))
op1 = num1%3==0
op2 = num1%5==0
if op1 and op2:
    print("El número es divisible por 3 y 5")
elif op2:
    print("El número es divisible por 5")
elif op1: 
    print("El número es divisible por 3")
else:
    print("El número no es divisible por 3 o 5")