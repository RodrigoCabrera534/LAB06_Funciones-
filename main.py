from utils import bienvenida, calcular_operaciones, validar_email

bienvenida()

# Parte 4: función extendida
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
suma, promedio, maximo, minimo = calcular_operaciones(num1, num2)
print(f"Suma     : {suma}")
print(f"Promedio : {promedio:.2f}")
print(f"Máximo   : {maximo}")
print(f"Mínimo   : {minimo}")

# Parte 3: validación de email
correo = input("\nIngresa un correo electrónico: ")
es_valido = validar_email(correo)
if es_valido:
    print(f"'{correo}' ES un correo válido.")
else:
    print(f"'{correo}' NO es un correo válido.")