#Escribe un programa que solicite al usuario tres números y determine cuál de ellos es el mayor.
print("A continuación escribe 3 números")
num1 = float(input("Escribe el primero número: "))
num2 = float(input("Escribe el segundo número: "))
num3 = float(input("Escribe el tercer número: "))
if num1 > num2 and num1 > num3:
    print ("El primer número es el mayor", "=", num1)
elif num2 > num3 and num2 > num1:
    print ("El segundo número es el mayor", "=", num2)
elif num3 > num1 and num3 > num2:
    print ("El tercer número es el mayor", "=", num3)
else:
    print ("Los números son iguales")