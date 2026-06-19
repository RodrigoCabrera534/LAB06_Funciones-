# utils.py - Módulo de funciones reutilizables
# Laboratorio 6 - Fundamentos de Programación
import re
def bienvenida():
    """
    Función sin parámetros que muestra un mensaje de bienvenida.
    Retorno: None
    """
    print("=" * 45)
    print("  Bienvenido al Sistema de Funciones - UPN ")
    print("  Fundamentos de Programación  2026-1    ")
    print("=" * 45)

def calcular_operaciones(a, b):
    """
    Función que recibe dos números y retorna su suma y promedio.
    Parámetros:
        a (float): primer número.
        b (float): segundo número.
    Retorno:
        tuple: contiene la suma y el promedio.
    """
    suma = a + b
    promedio = (a + b) / 2

    return suma, promedio

def validar_email(texto):
    """
    Función que valida si una cadena es un correo electrónico válido.

    Parámetros:
    texto (str): cadena a validar

    Retorno:
    bool: True si es un email válido, False en caso contrario
    """
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    resultado = bool(re.match(patron, texto))
    return resultado
