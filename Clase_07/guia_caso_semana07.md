# Guia paso a paso - Semana 07

## Caso: Analisis de emprendimientos costarricenses

**Archivo base del estudiante:** `clase07_analisis_emprendimientos.py`  
**Fuente de datos:** `sedes.py`

> Importante: no modifique `sedes.py`. Ese archivo representa la fuente de datos.
> Tampoco modifique el archivo original de referencia si el docente lo entrega como
> plantilla. Trabaje sobre una copia si desea conservar el punto de partida.

---

## 1. Que problema vamos a resolver

La red **EmprendeCR** agrupa varios emprendimientos costarricenses. Cada sede
registro sus ventas de lunes a viernes y tiene una meta semanal.

El programa debe responder:

1. Cuanto vendio cada sede en total.
2. Cual fue su promedio diario.
3. Que porcentaje de su meta alcanzo.
4. Si la sede alcanzo la meta, esta cerca o requiere atencion.
5. Que provincias aparecen en los datos.
6. Cual sede tuvo la venta total mas alta.

La solucion esperada no es solo imprimir numeros. Debe convertir datos en un
reporte claro para tomar decisiones.

---

## 2. Punto de partida

El archivo base `clase07_analisis_emprendimientos.py` empieza asi:

```python
"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes
```

### Por que empezamos con `from sedes import sedes`

Usamos un archivo separado para los datos porque en un programa real conviene
separar:

| Parte | Responsabilidad |
|---|---|
| `sedes.py` | Guardar los datos base. |
| `clase07_analisis_emprendimientos.py` | Resolver el analisis. |
| `analisis_emprendimientos_solucion.py` | Mostrar la solucion docente esperada. |

Esto ayuda a que el algoritmo sea mas limpio: el estudiante se concentra en
procesar datos, no en copiarlos.

---

## 3. Comprender la estructura de datos

Antes de calcular, debe entender que contiene `sedes`.

Cada sede es un diccionario parecido a este:

```python
{
    "nombre": "Soda San Pedro",
    "provincia": "San Jose",
    "tipo": "Alimentacion",
    "ventas": [85000, 92000, 78000, 110000, 97000],
    "meta": 450000,
}
```

### Para que sirve cada estructura

| Estructura | Donde aparece | Para que sirve |
|---|---|---|
| Lista | `sedes` | Guardar varias sedes y recorrerlas con `for`. |
| Diccionario | cada sede | Guardar campos con nombre: `nombre`, `provincia`, `ventas`, `meta`. |
| Lista | `ventas` | Guardar las ventas de lunes a viernes. |
| Set | `provincias` | Guardar provincias sin repetir. |
| Tupla | `(nombre, total)` | Guardar un par fijo para el ranking. |

### Primer bloque recomendado

Agregue debajo del import:

```python
print("Datos cargados:", len(sedes), "sedes")
print("Primera sede:", sedes[0])
```

### Por que hacerlo

Esto confirma que el import funciona y permite ver la forma real de los datos.
Si el programa falla aqui, no tiene sentido avanzar al calculo.

---

## 4. Crear la primera funcion: `calcular_total`

### Que debe hacer

Recibir una lista de ventas y retornar la suma.

```python
def calcular_total(ventas):
    """Retorna la suma de una lista de ventas."""
    return sum(ventas)
```

### Por que usar una funcion

Porque el total se necesita para todas las sedes. Si escribe `sum(...)` muchas
veces en diferentes partes, el codigo se vuelve repetitivo y mas dificil de
mantener.

### Para que sirve en el reporte

El total semanal permite saber cuanto vendio una sede y comparar ese resultado
contra la meta.

---

## 5. Crear `calcular_promedio`

### Que debe hacer

Recibir una lista de ventas y retornar el promedio.

```python
def calcular_promedio(ventas):
    """Retorna el promedio de una lista de ventas."""
    return sum(ventas) / len(ventas)
```

### Por que usar `len(ventas)`

Porque el promedio depende de la cantidad de datos. No conviene dividir entre
`5` de forma fija si luego el caso cambia a 6 o 7 dias.

### Para que sirve

El promedio diario ayuda a interpretar el comportamiento de la sede, no solo el
resultado acumulado.

---

## 6. Crear `calcular_porcentaje_cumplimiento`

### Que debe hacer

Calcular que porcentaje de la meta se alcanzo.

```python
def calcular_porcentaje_cumplimiento(total, meta):
    """Retorna el porcentaje de cumplimiento respecto a la meta."""
    return total / meta * 100
```

### Por que es importante

Dos sedes pueden tener totales diferentes, pero tambien metas diferentes. El
porcentaje permite comparar el avance de cada una de forma mas justa.

### Para que sirve

Permite imprimir mensajes como:

```text
Cumplimiento: 102.7%
```

### Prueba rapida

```python
assert calcular_porcentaje_cumplimiento(450000, 450000) == 100
```

---

## 7. Crear `clasificar_sede`

### Que debe hacer

Convertir el total y la meta en una decision.

```python
def clasificar_sede(total, meta):
    """Clasifica una sede segun su total semanal y su meta."""
    if total >= meta:
        return "Meta alcanzada"
    if total >= meta * 0.8:
        return "Cerca de la meta"
    return "Requiere atencion"
```

### Por que no basta con calcular

El analisis de datos no termina en numeros. Un algoritmo util ayuda a tomar una
decision. Aqui la decision es clasificar el estado de cada sede.

### Por que se usa condicional

Porque el programa debe tomar caminos distintos segun el resultado:

| Condicion | Resultado |
|---|---|
| `total >= meta` | `Meta alcanzada` |
| `total >= meta * 0.8` | `Cerca de la meta` |
| cualquier otro caso | `Requiere atencion` |

### Pruebas rapidas

```python
assert clasificar_sede(500000, 450000) == "Meta alcanzada"
assert clasificar_sede(380000, 450000) == "Cerca de la meta"
assert clasificar_sede(250000, 450000) == "Requiere atencion"
```

---

## 8. Crear `crear_reporte`

### Que debe hacer

Recorrer todas las sedes, calcular indicadores y construir una nueva lista con
los resultados procesados.

```python
def crear_reporte(sedes):
    """Construye los datos calculados para cada sede."""
    reporte = []

    for sede in sedes:
        total = calcular_total(sede["ventas"])
        promedio = calcular_promedio(sede["ventas"])
        porcentaje = calcular_porcentaje_cumplimiento(total, sede["meta"])
        estado = clasificar_sede(total, sede["meta"])

        reporte.append(
            {
                "nombre": sede["nombre"],
                "provincia": sede["provincia"],
                "tipo": sede["tipo"],
                "total": total,
                "promedio": promedio,
                "porcentaje": porcentaje,
                "estado": estado,
            }
        )

    return reporte
```

### Por que crear una lista nueva

Porque `sedes` contiene datos originales. El `reporte` contiene datos
procesados. Separar ambos evita modificar la fuente y deja claro que los
indicadores son resultados derivados.

### Por que usar un ciclo

Porque todas las sedes deben pasar por el mismo proceso. El ciclo evita copiar
el mismo codigo cinco veces.

### Que debe contener cada fila del reporte

| Campo | Origen |
|---|---|
| `nombre` | dato original |
| `provincia` | dato original |
| `tipo` | dato original |
| `total` | calculado |
| `promedio` | calculado |
| `porcentaje` | calculado |
| `estado` | decision condicional |

### Prueba rapida

```python
reporte = crear_reporte(sedes)
assert len(reporte) == len(sedes)
assert reporte[0]["nombre"] == "Soda San Pedro"
assert reporte[0]["total"] == 462000
```

---

## 9. Crear `mostrar_reporte`

### Que debe hacer

Imprimir el reporte principal de forma clara.

```python
def mostrar_reporte(reporte):
    """Imprime el reporte de analisis."""
    print("REPORTE DE EMPRENDIMIENTOS CR")
    print("-" * 72)

    for fila in reporte:
        print(f"Sede: {fila['nombre']}")
        print(f"Provincia: {fila['provincia']}")
        print(f"Tipo: {fila['tipo']}")
        print(f"Total semanal: C{fila['total']:,.0f}")
        print(f"Promedio diario: C{fila['promedio']:,.0f}")
        print(f"Cumplimiento: {fila['porcentaje']:.1f}%")
        print(f"Estado: {fila['estado']}")
        print("-" * 72)
```

### Por que separar mostrar de calcular

Una funcion calcula datos y otra los muestra. Esto permite revisar errores con
mas facilidad:

- si el calculo esta mal, revise `crear_reporte`;
- si el formato esta mal, revise `mostrar_reporte`.

### Para que sirven los f-strings

Permiten imprimir datos con texto claro y formato legible:

```python
C{fila['total']:,.0f}
{fila['porcentaje']:.1f}%
```

---

## 10. Crear `mostrar_resumen`

### Que debe hacer

Crear un resumen final con tres decisiones:

1. provincias presentes;
2. sedes que requieren atencion;
3. ranking de sedes por total.

```python
def mostrar_resumen(reporte):
    """Imprime resultados agregados usando set y tuplas."""
    provincias = set()
    sedes_atencion = []
    ranking = []

    for fila in reporte:
        provincias.add(fila["provincia"])
        ranking.append((fila["nombre"], fila["total"]))

        if fila["estado"] == "Requiere atencion":
            sedes_atencion.append(fila["nombre"])

    ranking_ordenado = sorted(ranking, key=lambda par: par[1], reverse=True)
    mejor_sede, mejor_total = ranking_ordenado[0]

    print("RESUMEN FINAL")
    print(f"Provincias presentes: {provincias}")
    print(f"Sedes que requieren atencion: {sedes_atencion}")
    print(f"Mejor sede: {mejor_sede} con C{mejor_total:,.0f}")
    print("Ranking:")

    for posicion, (nombre, total) in enumerate(ranking_ordenado, start=1):
        print(f"{posicion}. {nombre}: C{total:,.0f}")
```

### Por que usar `set`

Porque las provincias no deben repetirse. Si dos sedes fueran de San Jose, el
set guardaria `San Jose` una sola vez.

### Por que usar tuplas

`(nombre, total)` representa un par fijo: la sede y su total. Es suficiente para
crear el ranking sin cargar todos los campos otra vez.

### Por que aparece `sorted`

Se usa para ordenar el ranking de mayor a menor total. En esta guia aparece en
la solucion esperada, pero si el docente quiere bajar la dificultad, puede
pedir que el estudiante encuentre la mejor sede con un ciclo simple.

---

## 11. Crear `ejecutar_pruebas`

### Que debe hacer

Validar que las funciones principales funcionan antes de generar el reporte.

```python
def ejecutar_pruebas():
    """Validaciones minimas para la solucion docente."""
    assert calcular_total([100, 200, 300]) == 600
    assert calcular_promedio([100, 200, 300]) == 200
    assert calcular_porcentaje_cumplimiento(450000, 450000) == 100
    assert clasificar_sede(500000, 450000) == "Meta alcanzada"
    assert clasificar_sede(380000, 450000) == "Cerca de la meta"
    assert clasificar_sede(250000, 450000) == "Requiere atencion"
```

### Por que usar `assert`

`assert` permite comprobar rapidamente si una parte del programa hace lo que se
espera. Si una prueba falla, el programa se detiene y muestra que algo debe
revisarse.

No reemplaza una explicacion, pero ayuda a detectar errores antes de revisar el
reporte completo.

---

## 12. Ejecutar el programa completo

Al final del archivo agregue:

```python
if __name__ == "__main__":
    ejecutar_pruebas()
    reporte = crear_reporte(sedes)
    mostrar_reporte(reporte)
    mostrar_resumen(reporte)
```

### Por que usar `if __name__ == "__main__"`

Esta estructura indica que esas instrucciones se ejecutan cuando el archivo se
corre directamente. Es una buena practica para separar definiciones de
funciones y ejecucion principal.

### Orden correcto

1. Primero se prueban funciones.
2. Luego se crea el reporte.
3. Luego se imprime el reporte principal.
4. Al final se imprime el resumen.

---

## 13. Resultado esperado

Al ejecutar el programa, debe verse una salida con esta estructura:

```text
REPORTE DE EMPRENDIMIENTOS CR
------------------------------------------------------------------------
Sede: Soda San Pedro
Provincia: San Jose
Tipo: Alimentacion
Total semanal: C462,000
Promedio diario: C92,400
Cumplimiento: 102.7%
Estado: Meta alcanzada
------------------------------------------------------------------------
...
RESUMEN FINAL
Provincias presentes: {...}
Sedes que requieren atencion: []
Mejor sede: Marisqueria Puntarenas con C574,000
Ranking:
1. Marisqueria Puntarenas: C574,000
...
```

Los valores principales esperados son:

| Sede | Total | Estado |
|---|---:|---|
| Soda San Pedro | 462000 | Meta alcanzada |
| Panaderia Cartago | 351000 | Cerca de la meta |
| Cafeteria Liberia | 537000 | Meta alcanzada |
| Feria de Heredia | 380000 | Cerca de la meta |
| Marisqueria Puntarenas | 574000 | Meta alcanzada |

---

## 14. Checklist de implementacion

Marque cada punto al completar el archivo:

- [ ] El archivo importa `sedes` desde `sedes.py`.
- [ ] Cree `calcular_total`.
- [ ] Cree `calcular_promedio`.
- [ ] Cree `calcular_porcentaje_cumplimiento`.
- [ ] Cree `clasificar_sede`.
- [ ] Cree `crear_reporte`.
- [ ] Cree `mostrar_reporte`.
- [ ] Cree `mostrar_resumen`.
- [ ] Cree `ejecutar_pruebas`.
- [ ] Agregue el bloque `if __name__ == "__main__":`.
- [ ] Ejecute el programa sin errores.
- [ ] Compare la salida con el resultado esperado.

---

## 15. Preguntas de cierre

Responda con sus palabras:

1. Por que `sedes` es una lista?
2. Por que cada sede es un diccionario?
3. Para que sirve una funcion en este problema?
4. Donde se usa ejecucion condicional?
5. Donde se usa un ciclo?
6. Que ventaja tiene separar `crear_reporte` y `mostrar_reporte`?
7. Para que se uso el set?
8. Para que se usaron las tuplas?
