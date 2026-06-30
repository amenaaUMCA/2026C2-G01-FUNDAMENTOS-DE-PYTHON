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

def calcular_porcentaje(total, meta, formato = False):
    porcentaje = total / meta * 100
    if formato:
        return f"{porcentaje:.2f}%"
    return porcentaje

def calcular_clasificacion(total, meta):
    porcentaje = calcular_porcentaje(total, meta)
    if porcentaje >= 100: # pyright: ignore[reportOperatorIssue]
        mensaje_sede = "Meta alcanzada."
    elif porcentaje >= 80: # pyright: ignore[reportOperatorIssue]
        mensaje_sede = "Meta casi alcanzada, prestar atención."
    else:
        mensaje_sede = "Meta no alcanzada URGE ATENCION."
    return mensaje_sede

print("Cantidad de sedes:", len(sedes))
#print("Tipo de variable sedes:",type(sedes))
#print("Tipo de variable sedes[0]:",type(sedes[0]))
#print("Datos por sede:",sedes[0].keys())
#print("Primera sede:",sedes[0]['nombre'])
reporte = []
for sede in sedes:
    ventas = sede["ventas"]
    meta = sede['meta']

    total_sede = calcular_total(ventas)
    promedio_sede = calcular_promedio(ventas)
    porcentaje_sede = calcular_porcentaje(total_sede, meta, True)
    estado = calcular_clasificacion(total_sede, meta)

#print(imprimir_reporte(reporte))
#MAS ingresos
#Provincias