"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes


def calcular_total(ventas):
    """Recibo una lista, la sumo y retorno el total."""
    return sum(ventas)


def calcular_promedio(lista):
    """Retorna el promedio de ventas de una lista."""
    return sum(lista) / len(lista)


def calcular_porcentaje(total, meta):
    """Calcula el porcentaje de cumplimiento de una meta."""
    return total / meta * 100


def calcular_clasificacion(total, meta):
    """Clasifica la sede según el porcentaje de cumplimiento de la meta."""
    porcentaje = calcular_porcentaje(total, meta)

    if porcentaje >= 100:
        mensaje_sede = "Meta alcanzada."
    elif porcentaje >= 80:
        mensaje_sede = "Meta casi alcanzada, prestar atención."
    else:
        mensaje_sede = "Meta no alcanzada URGE ATENCION."

    return mensaje_sede


def imprimir_reporte(datos_reporte):
    """Imprime el reporte final de ventas por sede."""
    print("\nREPORTE FINAL")
    print("-" * 60)

    for fila in datos_reporte:
        print(f"Sede: {fila['nombre']}")
        print(f"Provincia: {fila['provincia']}")
        print(f"Tipo: {fila['tipo']}")
        print(f"Total semanal: ₡{fila['total']:,.0f}")
        print(f"Promedio diario: ₡{fila['promedio']:,.0f}")
        print(f"Cumplimiento: {fila['porcentaje']:.2f}%")
        print(f"Estado: {fila['estado']}")
        print("-" * 60)

    print("Cantidad de sedes:", len(datos_reporte))


reporte = []
provincias = set()
ranking = []

venta_mas_alta = 0
sedes_mas_ingresos = []

for sede in sedes:
    ventas = sede["ventas"]
    meta = sede["meta"]

    total_sede = calcular_total(ventas)
    promedio_sede = calcular_promedio(ventas)
    porcentaje_sede = calcular_porcentaje(total_sede, meta)
    estado = calcular_clasificacion(total_sede, meta)

    reporte.append(
        {
            "nombre": sede["nombre"],
            "provincia": sede["provincia"],
            "tipo": sede["tipo"],
            "total": total_sede,
            "promedio": promedio_sede,
            "porcentaje": porcentaje_sede,
            "estado": estado,
        }
    )

    provincias.add(sede["provincia"])
    ranking.append((sede["nombre"], total_sede))

    if total_sede > venta_mas_alta:
        venta_mas_alta = total_sede
        sedes_mas_ingresos = [sede["nombre"]]
    elif total_sede == venta_mas_alta:
        sedes_mas_ingresos.append(sede["nombre"])


imprimir_reporte(reporte)

print("\nRESUMEN FINAL")
print("Provincias analizadas:", provincias)
print("Ranking base:", ranking)
print(f"Venta más alta: ₡{venta_mas_alta:,.0f}")
print(
    "Sedes con más ingresos:",
    *sedes_mas_ingresos,
)
