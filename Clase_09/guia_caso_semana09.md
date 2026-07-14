# Guía de trabajo - Semana 09

## Mapeando datos y fijando valores

**Tema:** Dominando diccionarios y tuplas en Python

**Notebook:** `NOTEBOOK 06 - Conteo y Bucles Anidados.ipynb`

**Generador:** `generar_clinica_s09.py`

Trabajamos con una lista de hasta **1,000,000 de pacientes** y aplicamos una
idea central:

> Recorremos los registros, resumimos la información en diccionarios y
> consultamos esos resúmenes muchas veces.

Los primeros registros incluyen nombres del grupo para reconocer el conjunto.
**Las edades, ubicaciones, enfermedades, síntomas, medicamentos y demás datos
clínicos son sintéticos**. No representan información personal ni médica real.
El generador no almacena correos electrónicos ni indicadores académicos.

Al completar la práctica:

1. distinguimos listas, diccionarios, listas internas y tuplas;
2. acumulamos cantidades mediante claves dinámicas;
3. usamos ciclos anidados con listas y diccionarios de diccionarios;
4. construimos índices durante un único recorrido de los registros;
5. fijamos resultados como tuplas `(categoria, cantidad)`;
6. respondemos consultas desde los índices, sin volver al detalle original.

---

## Preparación técnica

### 1. Generamos los datos

Abrimos una terminal en `Semana 09` y ejecutamos:

```bash
python generar_clinica_s09.py
```

Al finalizar verificamos que:

- el progreso llega a `1,000,000`;
- existe `clinica_s09.json`;
- el archivo se generó por completo;
- no intentamos abrir el JSON completo en el editor.

La carga completa puede ocupar cerca de 1.5 GB de memoria. Cerramos otras
aplicaciones antes de cargarla cuando el equipo tiene memoria limitada.

### 2. Configuramos el notebook

En la **sección 1, celda de configuración y preparación**, dejamos el modo
oficial:

```python
NOMBRE_ARCHIVO_TRABAJO = "clinica_s09.json"
TOTAL_ESPERADO = 1_000_000
```

Ejecutamos en orden la configuración, la preparación y la carga. Antes de
continuar verificamos que el notebook muestre:

```text
Pacientes cargados: 1,000,000
```

Si reiniciamos el kernel, volvemos a ejecutar todas las celdas anteriores. La
variable `pacientes` solo existe después de completar la carga.

### 3. Usamos una muestra para ensayar

Después de cargar el archivo oficial podemos trabajar primero con:

```python
muestra = pacientes[:5_000]
```

Esta muestra acelera los primeros ensayos, pero **no reduce el uso de memoria**:
el millón ya está cargado en `pacientes`. La contingencia para memoria limitada
se explica al final de esta guía.

---

## Actividad 1 — Exploramos un registro

**Qué realizamos**

Seleccionamos el primer paciente y examinamos los tipos, las claves y la lista
interna de síntomas. Diferenciamos la colección completa de un registro y de
los valores que contiene.

**Dónde escribimos**

Completamos la **Actividad 1 — Exploramos un registro**.

**Requisitos verificables**

- identificamos `pacientes` como lista;
- identificamos un paciente como diccionario;
- mostramos las claves disponibles;
- identificamos `sintomas` como lista;
- consultamos al menos un valor del primer registro.

**Pistas conceptuales**

- Un índice numérico selecciona un elemento de una lista.
- Una clave selecciona un valor de un diccionario.
- `type()` y `.keys()` permiten inspeccionar sin modificar los datos.

---

## Actividad 2 — Mapeamos y fijamos

**Qué realizamos**

Recorremos un diccionario pequeño de pacientes por turno, representamos cada
par como tupla, desempaquetamos un resultado y comprobamos que una tupla no se
modifica por posición.

**Dónde escribimos**

Completamos la **Actividad 2 — Mapeamos y fijamos**.

**Requisitos verificables**

- recorremos el diccionario mediante `.items()`;
- construimos tuplas con forma `(turno, cantidad)`;
- desempaquetamos una tupla en dos variables;
- comprobamos la inmutabilidad capturando `TypeError`.

**Pistas conceptuales**

- El diccionario conserva asociaciones que podemos actualizar.
- `.items()` entrega la clave y el valor en cada vuelta.
- La tupla fija varios valores relacionados en una sola unidad.

---

## Actividad 3 — Contamos cualquier campo

**Qué realizamos**

Construimos una función reutilizable que cuenta los valores de un campo simple
en cualquier lista de registros.

**Dónde escribimos**

Completamos la celda de código de la **Actividad 3 — Contamos cualquier
campo**.

**Contrato**

```python
def contar_por_campo(registros, campo) -> dict:
    ...
```

**Requisitos verificables**

- devolvemos un diccionario `valor -> cantidad`;
- probamos la función con el campo `"enfermedad"` sobre `muestra`;
- la suma de las cantidades coincide con `len(muestra)`;
- ejecutamos:

  ```python
  verificar_contador(
      enfermedades_muestra, muestra, "enfermedad", "enfermedades de la muestra"
  )
  ```

**Pistas conceptuales**

- ¿Qué representa cada clave y qué representa cada cantidad en el resultado?
- ¿Qué debe ocurrir cuando encontramos una categoría por primera vez?
- Comprobamos que el total obtenido coincida con la cantidad de registros
  analizados.

---

## Actividad 4 — Contamos listas internas

**Qué realizamos**

Construimos una función que cuenta todas las ocurrencias de síntomas. Cada
registro contiene una lista, por lo que relacionamos un recorrido externo con
otro interno.

**Dónde escribimos**

Completamos la celda de código de la **Actividad 4 — Contamos listas
internas**.

**Contrato**

```python
def contar_sintomas(registros) -> dict:
    ...
```

**Requisitos verificables**

- devolvemos un diccionario `sintoma -> cantidad`;
- contamos ocurrencias, no pacientes únicos;
- la suma coincide con `len(muestra) * 3`;
- ejecutamos:

  ```python
  verificar_contador(
      sintomas_muestra,
      muestra,
      "sintomas",
      "síntomas de la muestra",
      campo_lista=True,
  )
  ```

**Pistas conceptuales**

- ¿Qué diferencia observamos entre contar registros y contar ocurrencias?
- ¿Qué estructura contiene los síntomas dentro de cada registro?
- Comprobamos que todas las ocurrencias presentes en las listas internas estén
  representadas en el resultado.

---

## Actividad 5 — Mapeamos provincia → enfermedad

**Qué realizamos**

Agrupamos los conteos de enfermedades dentro de cada provincia. El resultado
es un diccionario cuyos valores también son diccionarios.

**Dónde escribimos**

Completamos la celda de código de la **Actividad 5 — Mapeamos provincia →
enfermedad**.

**Contrato**

```python
def contar_enfermedades_por_provincia(registros) -> dict:
    ...
```

**Requisitos verificables**

- devolvemos `{provincia: {enfermedad: cantidad}}`;
- cada provincia posee su propio diccionario interno;
- los conteos internos suman `len(muestra)`;
- ejecutamos:

  ```python
  verificar_mapa_anidado(
      provincias_muestra,
      muestra,
      "provincia",
      "enfermedad",
      "mapa provincial de la muestra",
  )
  ```

**Pistas conceptuales**

- ¿Qué representa el primer nivel del mapa y qué representa el segundo?
- ¿Cómo distinguimos los conteos de una provincia de los conteos de otra?
- Comprobamos que cada combinación presente en los datos aparezca en el mapa.

---

## Actividad 6 — Integramos índices en un recorrido

**Qué realizamos**

Integramos los conteos de enfermedades, síntomas y enfermedades por provincia.
Procesamos cada registro una sola vez y devolvemos los tres índices juntos.

**Dónde escribimos**

Completamos la celda de código de la **Actividad 6 — Integramos índices en un
recorrido**.

**Contrato**

```python
def construir_indices(registros) -> tuple[dict, dict, dict]:
    ...
```

**Requisitos verificables**

- usamos un solo recorrido externo de `registros`;
- incluimos el recorrido interno necesario para los síntomas;
- devolvemos, en este orden, enfermedades, síntomas y mapa provincial;
- para el archivo oficial obtenemos totales `1,000,000`, `3,000,000` y
  `1,000,000` respectivamente;
- validamos los tres resultados con las llamadas a `verificar_contador` y
  `verificar_mapa_anidado` ya preparadas en la misma celda.

**Pistas conceptuales**

- ¿Qué tres resultados debe contener la tupla retornada?
- ¿Qué información de cada registro debe quedar representada en esos
  resultados?
- Comprobamos que exista un solo recorrido externo de `registros` y que los
  totales correspondan al conjunto analizado.

---

## Actividad 7 — Recorremos un diccionario anidado

**Qué realizamos**

Recorremos explícitamente los dos niveles de `conteo_por_provincia`, sumamos las
cantidades internas y construimos un total verificable para cada provincia.

**Dónde escribimos**

Completamos la celda de código de la **Actividad 7 — Recorremos un diccionario
anidado**.

**Requisitos verificables**

- construimos `totales_por_provincia` como un diccionario;
- usamos dos ciclos `for` explícitos: uno para
  `conteo_por_provincia.items()` y otro para el `.items()` del mapa interno;
- sumamos las cantidades internas y guardamos un total por provincia;
- no recorremos `pacientes` para producir este resumen;
- ejecutamos:

  ```python
  verificar_contador(
      totales_por_provincia,
      pacientes,
      "provincia",
      "totales calculados por provincia",
  )
  ```

**Pistas conceptuales**

- ¿Qué representa cada nivel de `conteo_por_provincia`?
- ¿Qué relación debe existir entre los conteos internos y el total de su
  provincia?
- Comprobamos que `totales_por_provincia` contenga exactamente las provincias
  presentes en el índice.

---

## Actividad 8 — Fijamos máximos y masificamos consultas

**Qué realizamos**

Construimos un máximo global, fijamos el resultado de cada grupo como tupla y
respondemos consultas usando los índices ya creados.

**Dónde escribimos**

Completamos la celda de código de la **Actividad 8 — Fijamos máximos y
masificamos consultas**.

**Contratos**

```python
def obtener_maximo(conteo) -> tuple[str, int]:
    ...


def obtener_maximos_por_grupo(
    mapa_anidado,
) -> dict[str, tuple[str, int]]:
    ...
```

**Requisitos verificables**

- recorremos los conteos mediante `.items()`;
- no usamos `max()`, `sorted()` ni `lambda` en el núcleo;
- devolvemos máximos con forma `(categoria, cantidad)`;
- `obtener_maximo({})` lanza `ValueError` con un mensaje claro que indique que
  no existe un máximo para un conteo vacío;
- verificamos el resultado global mediante `verificar_maximo(enfermedad_mas_frecuente, conteo_enfermedades, "máximo global")`;
- consultamos los casos de diabetes en San José desde `conteo_por_provincia`,
  sin recorrer `pacientes`.

**Pistas conceptuales**

- ¿Qué condiciones debe cumplir una tupla para representar el máximo?
- ¿Cómo comprobamos que cada grupo conserve su propio resultado?
- Reconocemos que un diccionario vacío no contiene un máximo válido.

---

## Actividad 9 — Resolvemos el reto individual

**Qué realizamos**

Construimos un nuevo índice anidado de medicamentos por enfermedad,
reutilizamos las funciones de máximos y consultamos el resultado de diabetes.

**Dónde escribimos**

Completamos la celda de código de la **Actividad 9 — Resolvemos el reto
individual**.

**Contrato de la séptima función**

```python
def construir_medicamentos_por_enfermedad(registros) -> dict:
    ...
```

**Requisitos verificables**

- devolvemos `{enfermedad: {medicamento: cantidad}}`;
- procesamos todos los registros cargados;
- reutilizamos `obtener_maximos_por_grupo`;
- consultamos la tupla correspondiente a `diabetes`;
- la suma de todos los conteos internos coincide con `len(pacientes)`;
- las enfermedades del nuevo mapa coinciden con las de
  `conteo_enfermedades`;
- validamos el mapa con:

  ```python
  verificar_mapa_anidado(
      medicamentos_por_enfermedad,
      pacientes,
      "enfermedad",
      "medicamento",
      "medicamentos por enfermedad",
  )
  ```

**Pistas conceptuales**

- La forma requerida coincide con otro mapa anidado que ya construimos.
- Cada registro aporta exactamente un medicamento a una enfermedad.
- Reutilizar una función evita resolver nuevamente el mismo problema.

---

## Actividad 10 — Cerramos con el ticket de salida

**Qué realizamos**

Explicamos con nuestras palabras cuatro decisiones tomadas durante la práctica.

**Dónde escribimos**

Completamos la celda de código de la **Actividad 10 — Cerramos con el ticket de
salida**.

**Requisitos verificables**

Respondemos las cuatro frases con ideas distintas y relacionadas con nuestro
código:

1. “Usamos un diccionario cuando necesitamos...”
2. “Usamos una tupla cuando necesitamos...”
3. “El ciclo anidado fue necesario porque...”
4. “Podemos consultar muchas veces sin recorrer el millón porque...”

**Pistas conceptuales**

- Relacionamos cada respuesta con una estructura o recorrido que usamos.
- Explicamos el propósito de la decisión, no repetimos una definición aislada.
- Distinguimos el detalle original de los índices construidos.

---

## Comprobamos nuestro trabajo

Comprobamos la forma de cada estructura y verificamos que sus totales
correspondan al conjunto cargado. No dependemos de valores finales escritos en
la guía: las funciones de verificación comparan nuestros resultados con los
datos procesados.

Las funciones auxiliares disponibles en el notebook provienen del módulo de
apoyo `verificaciones_s09.py`:

```python
verificar_contador(conteo, registros, campo, etiqueta, campo_lista=False)
verificar_mapa_anidado(mapa, registros, campo_grupo, campo_valor, etiqueta)
verificar_maximo(resultado, conteo, etiqueta)
```

Las usamos después de construir cada resultado. Estas funciones comprueban la
estructura y los totales, pero no reemplazan nuestras implementaciones.

---

## Señales para revisar nuestro trabajo

| Señal observable | Pregunta de revisión |
|---|---|
| `NameError: pacientes is not defined` | ¿La variable `pacientes` existe en la memoria del kernel? |
| Aparece un `KeyError` | ¿Nuestro código contempla categorías que todavía no están representadas? |
| Todos los conteos quedan en `1` | ¿Las cantidades reflejan todas las apariciones observadas en los datos? |
| El diccionario queda vacío | ¿La función produce y entrega una estructura con las categorías esperadas? |
| El total de síntomas no coincide | ¿El resultado representa todas las ocurrencias de las listas internas? |
| Faltan provincias o combinaciones | ¿El mapa contiene todos los grupos y pares presentes en los datos? |
| `construir_indices` realiza varios recorridos externos | ¿Cumplimos el requisito de un único recorrido externo de `registros`? |
| El máximo no supera la verificación | ¿La tupla pertenece al conteo y representa su cantidad mayor? |
| Una consulta vuelve al detalle original | ¿El índice construido ya contiene la información solicitada? |

---

## Contingencia para memoria limitada

`pacientes[:5_000]` no resuelve un problema de memoria porque requiere cargar
primero el millón. Para trabajar realmente con 10,000 registros generamos un
archivo separado desde `Semana 09`:

```bash
python generar_clinica_s09.py --total 10000 --destino clinica_s09_muestra_10000.json
```

Después configuramos la **sección 1 del notebook** antes de cargar:

```python
NOMBRE_ARCHIVO_TRABAJO = "clinica_s09_muestra_10000.json"
TOTAL_ESPERADO = 10_000
```

En este modo, el notebook mantiene `muestra` con los primeros 5,000 registros
del archivo de 10,000. Las verificaciones se basan en el conjunto que recibe
cada función y continúan funcionando. Para la evidencia final restauramos:

```python
NOMBRE_ARCHIVO_TRABAJO = "clinica_s09.json"
TOTAL_ESPERADO = 1_000_000
```

Si el JSON está incompleto, no intentamos analizarlo. Volvemos a ejecutar el
generador; este escribe primero en un archivo temporal y publica el destino
solo cuando termina. Si la carga produce `MemoryError`, cerramos aplicaciones,
reiniciamos el kernel y usamos el modo de 10,000 registros hasta disponer de un
equipo que permita la verificación final.

---

## Extensión opcional

Después de completar el núcleo, reproducimos el conteo de enfermedades con
`collections.Counter`, obtenemos cinco frecuencias con `sorted()` y `lambda`, y
comparamos el resultado con `conteo_enfermedades`.

Escribimos esta exploración únicamente en la **sección “Extensión opcional”**
del notebook. La extensión no sustituye ninguna de las siete funciones.
