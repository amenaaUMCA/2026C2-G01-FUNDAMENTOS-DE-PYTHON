"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""
from sedes import sedes


def calcular_total(ventas):
    """Recibo una lista, la sumo y retorno el total"""
    return sum(ventas)

def calcular_promedio(lista):
    """Retorna el promedio de ventas de una lista"""
    return sum(lista) / len(lista)

print("Cantidad de sedes:", len(sedes))
print("Tipo de variable sedes:",type(sedes))
print("Tipo de variable sedes[0]:",type(sedes[0]))
print("Datos por sede:",sedes[0].keys())
print("Primera sede:",sedes[0]['nombre'])

sede_demo = sedes[0]
ventas = sede_demo["ventas"]
meta = sede_demo['meta']

total_sede = calcular_total(ventas)
promedio_sede = total_sede / len(ventas)
porcentaje_sede = total_sede / meta * 100

if porcentaje_sede >= 100:
    mensaje_sede = "Meta alcanzada."
elif porcentaje_sede >= 80:
    mensaje_sede = "Meta casi alcanzada, prestar atención."
else:
    mensaje_sede = "Meta no alcanzada URGE ATENCION."

print(porcentaje_sede, total_sede)  #[85000, 92000, 78000, 110000, 97000]