# main.py - Archivo principal

from utils import bienvenida, calcular_operaciones

bienvenida()

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

suma, promedio = calcular_operaciones(num1, num2)

print(f"Suma : {suma}")
print(f"Promedio : {promedio:.2f}")
