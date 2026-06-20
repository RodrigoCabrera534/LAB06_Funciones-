# utils.py - Módulo de funciones reutilizables
# Laboratorio 6 - Fundamentos de Programación
import re
import math


def bienvenida():
    """
    Función sin parámetros que muestra un mensaje de bienvenida.
    Retorno: None
    """
    print("=" * 45)
    print(" Bienvenido al Sistema de Funciones - UPN ")
    print(" Fundamentos de Programación 2026-1 ")
    print("=" * 45)


def calcular_operaciones(a, b):
    """
    Función que recibe dos números y retorna su suma, promedio, máximo y mínimo.
    Parámetros:
        a (float): primer número
        b (float): segundo número
    Retorno:
        tuple: (suma, promedio, maximo, minimo)
    """
    suma = a + b
    promedio = (a + b) / 2
    maximo = a if a > b else b
    minimo = a if a < b else b
    return suma, promedio, maximo, minimo


def validar_email(texto):
    """
    Función que valida si una cadena es un correo electrónico válido.
    Parámetros:
        texto (str): cadena a validar
    Retorno:
        bool: True si es un email válido, False en caso contrario
    """
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, texto))


def calcular_estadisticas(numeros):
    """
    Función que recibe una lista de números y calcula estadísticas.
    Parámetros:
        numeros (list): lista de números enteros o flotantes
    Retorno:
        dict: diccionario con total, promedio, maximo, minimo
    """
    total = math.fsum(numeros)
    prom = total / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)

    return {
        "total": total,
        "promedio": round(prom, 2),
        "maximo": maximo,
        "minimo": minimo
    }