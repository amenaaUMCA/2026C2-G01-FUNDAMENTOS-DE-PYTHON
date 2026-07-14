"""Solucion docente: diccionarios y tuplas con datos clinicos masivos.

Los nombres reales solo identifican algunos registros. Toda la informacion
clinica generada es sintetica y no describe a ninguna persona.
"""

import json
from pathlib import Path

from verificaciones_s09 import (
    verificar_contador,
    verificar_mapa_anidado,
    verificar_maximo,
    verificar_maximos,
)


ARCHIVO_DATOS = Path(__file__).with_name("clinica_s09.json")
TOTAL_ESPERADO = 1_000_000


def cargar_pacientes(ruta=ARCHIVO_DATOS, total_esperado=TOTAL_ESPERADO):
    """Carga y valida una lista de pacientes desde un archivo JSON."""
    try:
        with Path(ruta).open("r", encoding="utf-8") as archivo:
            pacientes = json.load(archivo)
    except FileNotFoundError as error:
        raise FileNotFoundError(
            "No se encontro clinica_s09.json. Ejecute generar_clinica_s09.py."
        ) from error
    except json.JSONDecodeError as error:
        raise ValueError(
            "El JSON esta incompleto. Genere nuevamente el archivo."
        ) from error
    except MemoryError as error:
        raise MemoryError(
            "No hay memoria suficiente. Cierre otras aplicaciones e intente "
            "de nuevo."
        ) from error

    if not isinstance(pacientes, list):
        raise TypeError("El JSON debe contener una lista de pacientes.")
    if total_esperado is not None and len(pacientes) != total_esperado:
        raise ValueError(
            f"Se esperaban {total_esperado:,} pacientes, pero se encontraron "
            f"{len(pacientes):,}."
        )

    return pacientes


# ACTIVIDAD 3 - Contamos cualquier campo
def contar_por_campo(registros, campo) -> dict:
    """Retorna un diccionario valor -> cantidad para el campo indicado."""
    conteo = {}

    for registro in registros:
        valor = registro[campo]
        conteo[valor] = conteo.get(valor, 0) + 1

    return conteo


# ACTIVIDAD 4 - Contamos listas internas
def contar_sintomas(registros) -> dict:
    """Cuenta las apariciones de sintomas mediante ciclos anidados."""
    conteo = {}

    for paciente in registros:
        for sintoma in paciente["sintomas"]:
            conteo[sintoma] = conteo.get(sintoma, 0) + 1

    return conteo


# ACTIVIDAD 5 - Mapeamos provincia -> enfermedad
def contar_enfermedades_por_provincia(registros) -> dict:
    """Retorna el mapa provincia -> enfermedad -> cantidad."""
    conteo_por_provincia = {}

    for paciente in registros:
        provincia = paciente["provincia"]
        enfermedad = paciente["enfermedad"]

        if provincia not in conteo_por_provincia:
            conteo_por_provincia[provincia] = {}

        conteo_enfermedades = conteo_por_provincia[provincia]
        conteo_enfermedades[enfermedad] = (
            conteo_enfermedades.get(enfermedad, 0) + 1
        )

    return conteo_por_provincia


# ACTIVIDAD 6 - Integramos indices en un recorrido
def construir_indices(registros) -> tuple[dict, dict, dict]:
    """Construye tres indices en un unico ciclo externo sobre registros."""
    conteo_enfermedades = {}
    conteo_sintomas = {}
    conteo_por_provincia = {}

    for paciente in registros:
        enfermedad = paciente["enfermedad"]
        provincia = paciente["provincia"]

        conteo_enfermedades[enfermedad] = (
            conteo_enfermedades.get(enfermedad, 0) + 1
        )

        if provincia not in conteo_por_provincia:
            conteo_por_provincia[provincia] = {}

        enfermedades_provincia = conteo_por_provincia[provincia]
        enfermedades_provincia[enfermedad] = (
            enfermedades_provincia.get(enfermedad, 0) + 1
        )

        for sintoma in paciente["sintomas"]:
            conteo_sintomas[sintoma] = conteo_sintomas.get(sintoma, 0) + 1

    return conteo_enfermedades, conteo_sintomas, conteo_por_provincia


# ACTIVIDAD 8 - Fijamos maximos y masificamos consultas
def obtener_maximo(conteo) -> tuple[str, int]:
    """Retorna una tupla (categoria, cantidad) sin max, lambda ni Counter."""
    if not conteo:
        raise ValueError("No podemos obtener un máximo de un conteo vacío.")

    categoria_mayor = ""
    cantidad_mayor = -1

    for categoria, cantidad in conteo.items():
        if cantidad > cantidad_mayor:
            categoria_mayor = categoria
            cantidad_mayor = cantidad

    return categoria_mayor, cantidad_mayor


def obtener_maximos_por_grupo(
    mapa_anidado,
) -> dict[str, tuple[str, int]]:
    """Retorna grupo -> (categoria, cantidad) para un mapa anidado."""
    maximos_por_grupo = {}

    for grupo, conteo in mapa_anidado.items():
        try:
            maximos_por_grupo[grupo] = obtener_maximo(conteo)
        except ValueError as error:
            raise ValueError(
                f"No podemos obtener el máximo del grupo {grupo!r}: "
                "está vacío."
            ) from error

    return maximos_por_grupo


# ACTIVIDAD 9 - Resolvemos el reto individual
def construir_medicamentos_por_enfermedad(registros) -> dict:
    """Retorna el mapa enfermedad -> medicamento -> cantidad."""
    medicamentos_por_enfermedad = {}

    for paciente in registros:
        enfermedad = paciente["enfermedad"]
        medicamento = paciente["medicamento"]

        if enfermedad not in medicamentos_por_enfermedad:
            medicamentos_por_enfermedad[enfermedad] = {}

        conteo_medicamentos = medicamentos_por_enfermedad[enfermedad]
        conteo_medicamentos[medicamento] = (
            conteo_medicamentos.get(medicamento, 0) + 1
        )

    return medicamentos_por_enfermedad


def verificar_resultados(
    pacientes,
    conteo_enfermedades,
    conteo_sintomas,
    conteo_por_provincia,
    enfermedad_mas_frecuente,
    maximos_por_provincia,
    medicamentos_por_enfermedad,
    medicamentos_principales,
):
    """Comprueba exactamente los índices construidos contra los registros."""
    verificar_contador(
        conteo_enfermedades,
        pacientes,
        "enfermedad",
        "enfermedades",
    )
    verificar_contador(
        conteo_sintomas,
        pacientes,
        "sintomas",
        "sintomas",
        campo_lista=True,
    )
    verificar_mapa_anidado(
        conteo_por_provincia,
        pacientes,
        "provincia",
        "enfermedad",
        "enfermedades por provincia",
    )
    verificar_maximo(
        enfermedad_mas_frecuente,
        conteo_enfermedades,
        "maximo global",
    )
    verificar_maximos(
        maximos_por_provincia,
        conteo_por_provincia,
        "maximos por provincia",
    )
    verificar_mapa_anidado(
        medicamentos_por_enfermedad,
        pacientes,
        "enfermedad",
        "medicamento",
        "medicamentos por enfermedad",
    )
    verificar_maximos(
        medicamentos_principales,
        medicamentos_por_enfermedad,
        "medicamentos principales",
    )


def main():
    """Carga el millon, construye indices y ejecuta consultas masivas."""
    try:
        pacientes = cargar_pacientes()
    except (FileNotFoundError, ValueError, TypeError, MemoryError) as error:
        print("No fue posible iniciar la practica:", error)
        return

    print("ADVERTENCIA: todos los datos clinicos son sinteticos.")
    print(f"Pacientes cargados: {len(pacientes):,}")
    print("Campos disponibles:", tuple(pacientes[0].keys()))

    # ACTIVIDAD 1 - Exploramos un registro
    primer_paciente = pacientes[0]
    print("Coleccion:", type(pacientes).__name__)
    print("Registro:", type(primer_paciente).__name__)
    print("Campos:", tuple(primer_paciente.keys()))
    print("Sintomas:", type(primer_paciente["sintomas"]).__name__)
    print("Primer sintoma:", primer_paciente["sintomas"][0])

    # ACTIVIDAD 2 - Mapeamos y fijamos
    pacientes_por_turno = {"mañana": 18, "tarde": 25}
    tupla_mayor = ("", -1)

    for turno, cantidad in pacientes_por_turno.items():
        par_fijo = (turno, cantidad)
        print(par_fijo)
        if cantidad > tupla_mayor[1]:
            tupla_mayor = par_fijo

    turno_mayor, cantidad_mayor = tupla_mayor
    print("Turno con mas pacientes:", turno_mayor, cantidad_mayor)
    try:
        tupla_mayor[1] = 30
    except TypeError:
        print("La tupla no permite cambiar la cantidad.")

    # ACTIVIDAD 3 - Contamos cualquier campo
    muestra = pacientes[:5_000]
    enfermedades_muestra = contar_por_campo(muestra, "enfermedad")

    # ACTIVIDAD 4 - Contamos listas internas
    sintomas_muestra = contar_sintomas(muestra)

    # ACTIVIDAD 5 - Mapeamos provincia -> enfermedad
    provincias_muestra = contar_enfermedades_por_provincia(muestra)

    print("\nPRACTICA CON 5,000 REGISTROS")
    print("Diagnosticos:", sum(enfermedades_muestra.values()))
    print("Sintomas:", sum(sintomas_muestra.values()))
    print("Provincias:", len(provincias_muestra))

    # ACTIVIDAD 6 - Integramos indices en un recorrido
    resumenes = construir_indices(pacientes)
    conteo_enfermedades, conteo_sintomas, conteo_por_provincia = resumenes

    # ACTIVIDAD 7 - Recorremos un diccionario anidado
    totales_por_provincia = {}
    for provincia, mapa in conteo_por_provincia.items():
        total_provincia = 0
        for enfermedad, cantidad in mapa.items():
            total_provincia += cantidad
        totales_por_provincia[provincia] = total_provincia

    verificar_contador(
        totales_por_provincia,
        pacientes,
        "provincia",
        "totales calculados por provincia",
    )

    # ACTIVIDAD 8 - Fijamos maximos y masificamos consultas
    enfermedad_mas_frecuente = obtener_maximo(conteo_enfermedades)
    maximos_por_provincia = obtener_maximos_por_grupo(conteo_por_provincia)

    # ACTIVIDAD 9 - Resolvemos el reto individual
    medicamentos_por_enfermedad = construir_medicamentos_por_enfermedad(
        pacientes
    )
    medicamentos_principales = obtener_maximos_por_grupo(
        medicamentos_por_enfermedad
    )

    verificar_resultados(
        pacientes,
        conteo_enfermedades,
        conteo_sintomas,
        conteo_por_provincia,
        enfermedad_mas_frecuente,
        maximos_por_provincia,
        medicamentos_por_enfermedad,
        medicamentos_principales,
    )

    print("\nRESUMEN MASIVO")
    print("Diagnosticos contabilizados:", sum(conteo_enfermedades.values()))
    print("Enfermedades distintas:", len(conteo_enfermedades))
    print("Ocurrencias de sintomas:", sum(conteo_sintomas.values()))
    print("Sintomas distintos:", len(conteo_sintomas))
    print("Provincias:", len(conteo_por_provincia))
    print("Enfermedad mas frecuente:", enfermedad_mas_frecuente)

    print("\nCONSULTAS SIN RECORRER DE NUEVO EL JSON")
    print("Casos de diabetes:", conteo_enfermedades.get("diabetes", 0))
    print("Casos de fiebre:", conteo_sintomas.get("fiebre", 0))
    print(
        "Diabetes en San Jose:",
        conteo_por_provincia.get("San Jos\u00e9", {}).get("diabetes", 0),
    )

    print("\nMAXIMOS POR PROVINCIA")
    for provincia, resultado in maximos_por_provincia.items():
        enfermedad, cantidad = resultado
        print(provincia + ":", enfermedad, "-", cantidad)

    print("\nRETO: MEDICAMENTOS POR ENFERMEDAD")
    print("Enfermedades consultables:", len(medicamentos_por_enfermedad))
    print(
        "Medicamento principal para diabetes:",
        medicamentos_principales.get("diabetes", ("", 0)),
    )

    # ACTIVIDAD 10 - Cerramos con el ticket de salida
    respuesta_diccionario = (
        "asocia cada categoria con un conteo consultable por su clave."
    )
    respuesta_tupla = (
        "mantiene juntos la categoria maxima y su cantidad como resultado fijo."
    )
    respuesta_ciclo_anidado = (
        "recorre cada registro y luego los valores contenidos en ese registro."
    )
    respuesta_consulta_masiva = (
        "responde desde el resumen sin recorrer nuevamente todos los pacientes."
    )

    print("Elegimos un diccionario porque", respuesta_diccionario)
    print("Elegimos una tupla porque", respuesta_tupla)
    print("Usamos un ciclo anidado porque", respuesta_ciclo_anidado)
    print("Consultamos el indice masivo porque", respuesta_consulta_masiva)


if __name__ == "__main__":
    main()
