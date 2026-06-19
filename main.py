from utils import bienvenida, calcular_operaciones

bienvenida()

while True:

    num1 = float(input("\nIngresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    suma, promedio = calcular_operaciones(num1, num2)

    print(f"Suma     : {suma}")
    print(f"Promedio : {promedio:.2f}")

    continuar = input("\n¿Deseas hacer otra prueba? (si = 1/no = 2): ")

    if continuar.lower() != "1":
        break