#Escribe un programa que tome una calificación numérica de un estudiante (entre 0 y 100) y le asigne una letra
num1= int(input("Escribe tu nota para saber tu calificación: "))
if num1 >=90 and num1 <= 100:
    print("A")
elif num1 >80:
    print("B")
elif num1 >70:
    print("C")
elif num1 >60:
    print("D")
else:
    print("F")