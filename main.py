# main.py - Programa de integración final

from utils import (
    bienvenida,
    calcular_operaciones,
    validar_email,
    calcular_estadisticas
)

# 1. Bienvenida
bienvenida()

# 2. Operaciones numéricas
a, b = 15.0, 25.0
suma, prom, maximo, minimo = calcular_operaciones(a, b)

print(f"\nOperaciones con {a} y {b}:")
print(f"  Suma={suma}  Promedio={prom}  Max={maximo}  Min={minimo}")

# 3. Validación de emails
correos = ["alumno@upn.pe", "invalido-sin-arroba", "test@gmail.com"]
print("\nValidación de correos:")
for c in correos:
    print(f"  {c} -> {'Válido' if validar_email(c) else 'Inválido'}")

# 4. Estadísticas de lista
datos = [10, 45, 23, 67, 89, 12, 34]
stats = calcular_estadisticas(datos)

print(f"\nEstadísticas de {datos}:")
for k, v in stats.items():
    print(f"  {k}: {v}")