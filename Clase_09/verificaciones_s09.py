"""Verificaciones reutilizables para las actividades de la Semana 09."""

from collections import Counter


def _contador_esperado(registros, campo, campo_lista=False):
    if campo_lista:
        return Counter(
            valor
            for registro in registros
            for valor in registro[campo]
        )
    return Counter(registro[campo] for registro in registros)


def verificar_contador(
    conteo, registros, campo, etiqueta, campo_lista=False
):
    """Comprueba estructura, tipos y cantidades exactas de un contador."""
    if not isinstance(conteo, dict):
        raise AssertionError(f"Revisamos {etiqueta}: debe ser un diccionario.")

    esperado = _contador_esperado(registros, campo, campo_lista)
    if set(conteo) != set(esperado):
        raise AssertionError(
            f"Revisamos {etiqueta}: faltan claves o aparecen claves inesperadas."
        )
    if any(type(cantidad) is not int or cantidad < 0 for cantidad in conteo.values()):
        raise AssertionError(
            f"Revisamos {etiqueta}: cada cantidad debe ser un entero no negativo."
        )
    if conteo != dict(esperado):
        raise AssertionError(
            f"Revisamos {etiqueta}: una o más cantidades no corresponden a los datos."
        )

    total = sum(esperado.values())
    if sum(conteo.values()) != total:
        raise AssertionError(
            f"Revisamos {etiqueta}: los conteos deben sumar {total:,}."
        )
    print(f"Correcto: {etiqueta} contiene {len(conteo)} claves y suma {total:,}.")


def verificar_mapa_anidado(
    mapa, registros, campo_grupo, campo_valor, etiqueta
):
    """Comprueba cada cantidad exacta de un mapa grupo-categoría."""
    if not isinstance(mapa, dict):
        raise AssertionError(f"Revisamos {etiqueta}: debe ser un diccionario.")

    esperado = Counter(
        (registro[campo_grupo], registro[campo_valor])
        for registro in registros
    )
    grupos_esperados = {grupo for grupo, _ in esperado}
    if set(mapa) != grupos_esperados:
        raise AssertionError(
            f"Revisamos {etiqueta}: faltan grupos o aparecen grupos inesperados."
        )
    if any(not isinstance(conteos, dict) for conteos in mapa.values()):
        raise AssertionError(
            f"Revisamos {etiqueta}: cada grupo debe contener otro diccionario."
        )

    obtenido = {}
    for grupo, conteos in mapa.items():
        for categoria, cantidad in conteos.items():
            if type(cantidad) is not int or cantidad < 0:
                raise AssertionError(
                    f"Revisamos {etiqueta}: cada cantidad debe ser un entero no negativo."
                )
            obtenido[(grupo, categoria)] = cantidad

    if set(obtenido) != set(esperado):
        raise AssertionError(
            f"Revisamos {etiqueta}: las combinaciones internas no corresponden a los datos."
        )
    if obtenido != dict(esperado):
        raise AssertionError(
            f"Revisamos {etiqueta}: una o más cantidades internas son incorrectas."
        )
    if sum(obtenido.values()) != len(registros):
        raise AssertionError(
            f"Revisamos {etiqueta}: los conteos deben sumar {len(registros):,}."
        )
    print(
        f"Correcto: {etiqueta} contiene {len(mapa)} grupos "
        f"y suma {len(registros):,}."
    )


def verificar_maximo(resultado, conteo, etiqueta):
    """Comprueba que una tupla represente un máximo del contador."""
    if not conteo:
        raise AssertionError(f"Revisamos {etiqueta}: el conteo está vacío.")
    if not isinstance(resultado, tuple) or len(resultado) != 2:
        raise AssertionError(
            f"Revisamos {etiqueta}: debe ser una tupla de dos elementos."
        )
    clave, cantidad = resultado
    if (
        clave not in conteo
        or conteo[clave] != cantidad
        or cantidad != max(conteo.values())
    ):
        raise AssertionError(
            f"Revisamos {etiqueta}: la tupla no representa el máximo."
        )
    print(f"Correcto: {etiqueta} = {resultado}")


def verificar_maximos(maximos, mapa_anidado, etiqueta):
    """Comprueba la tupla máxima de cada grupo de un mapa anidado."""
    if not isinstance(maximos, dict) or set(maximos) != set(mapa_anidado):
        raise AssertionError(f"Revisamos {etiqueta}: faltan o sobran grupos.")
    for grupo, resultado in maximos.items():
        verificar_maximo(resultado, mapa_anidado[grupo], f"{etiqueta}: {grupo}")
