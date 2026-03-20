"""
Árbol de Decisión (Decision Tree)
Clasificador supervisado que divide los datos de forma recursiva
usando la ganancia de información (entropía de Shannon).
"""
import math
from collections import Counter


def entropia(etiquetas):
    """Calcula la entropía de un conjunto de etiquetas."""
    conteo = Counter(etiquetas)
    total = len(etiquetas)
    return -sum((c / total) * math.log2(c / total) for c in conteo.values() if c > 0)


def ganancia_informacion(datos, etiquetas, caracteristica):
    """Calcula la ganancia de información para dividir por una característica."""
    entropia_original = entropia(etiquetas)
    valores = set(d[caracteristica] for d in datos)
    total = len(datos)

    entropia_ponderada = 0
    for valor in valores:
        indices = [i for i, d in enumerate(datos) if d[caracteristica] == valor]
        sub_etiquetas = [etiquetas[i] for i in indices]
        entropia_ponderada += (len(indices) / total) * entropia(sub_etiquetas)

    return entropia_original - entropia_ponderada


def construir_arbol(datos, etiquetas, caracteristicas, profundidad=0, max_profundidad=5):
    """
    Construye recursivamente un árbol de decisión.

    Args:
        datos: lista de dicts con características
        etiquetas: lista de clases correspondientes
        caracteristicas: lista de características disponibles
        profundidad: profundidad actual del árbol
        max_profundidad: profundidad máxima permitida

    Returns:
        nodo del árbol (dict o valor de clase)
    """
    if not etiquetas:
        return None

    # Caso base: todos pertenecen a la misma clase
    if len(set(etiquetas)) == 1:
        return etiquetas[0]

    # Caso base: sin características o profundidad máxima
    if not caracteristicas or profundidad >= max_profundidad:
        return Counter(etiquetas).most_common(1)[0][0]

    # Seleccionar la mejor característica
    mejor = max(caracteristicas, key=lambda c: ganancia_informacion(datos, etiquetas, c))
    resto = [c for c in caracteristicas if c != mejor]

    nodo = {'caracteristica': mejor, 'ramas': {}}
    for valor in set(d[mejor] for d in datos):
        indices = [i for i, d in enumerate(datos) if d[mejor] == valor]
        sub_datos = [datos[i] for i in indices]
        sub_etiquetas = [etiquetas[i] for i in indices]
        nodo['ramas'][valor] = construir_arbol(
            sub_datos, sub_etiquetas, resto, profundidad + 1, max_profundidad
        )

    return nodo


def clasificar(nodo, muestra):
    """Clasifica una muestra usando el árbol construido."""
    if not isinstance(nodo, dict):
        return nodo
    valor = muestra.get(nodo['caracteristica'])
    rama = nodo['ramas'].get(valor)
    if rama is None:
        return None
    return clasificar(rama, muestra)


if __name__ == "__main__":
    # Ejemplo: clasificar si salir a jugar según el clima
    datos = [
        {'clima': 'soleado', 'viento': 'bajo'},
        {'clima': 'soleado', 'viento': 'alto'},
        {'clima': 'nublado', 'viento': 'bajo'},
        {'clima': 'nublado', 'viento': 'alto'},
        {'clima': 'lluvioso', 'viento': 'bajo'},
        {'clima': 'lluvioso', 'viento': 'alto'},
    ]
    etiquetas = ['si', 'no', 'si', 'si', 'si', 'no']

    arbol = construir_arbol(datos, etiquetas, ['clima', 'viento'])

    prueba = {'clima': 'soleado', 'viento': 'bajo'}
    resultado = clasificar(arbol, prueba)
    print(f"¿Salir a jugar con {prueba}? -> {resultado}")

    prueba2 = {'clima': 'lluvioso', 'viento': 'alto'}
    resultado2 = clasificar(arbol, prueba2)
    print(f"¿Salir a jugar con {prueba2}? -> {resultado2}")
