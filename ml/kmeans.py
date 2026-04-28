"""
K-Means Clustering
Algoritmo de clustering no supervisado que agrupa datos
en K grupos según su similitud basada en distancia euclidiana.
"""
import random
import math


def distancia_euclidiana(punto1, punto2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(punto1, punto2)))


def calcular_centroide(puntos):
    n = len(puntos)
    dimensiones = len(puntos[0])
    return [sum(p[d] for p in puntos) / n for d in range(dimensiones)]


def kmeans(datos, k, max_iteraciones=100, semilla=42):
    """
    Agrupa los datos en K clusters usando el algoritmo K-Means.

    Args:
        datos: lista de puntos (listas de floats)
        k: número de clusters
        max_iteraciones: límite de iteraciones
        semilla: semilla para reproducibilidad

    Returns:
        (centroides, etiquetas) centroides finales y asignación de cada punto
    """
    random.seed(semilla)
    centroides = random.sample(datos, k)

    etiquetas = [0] * len(datos)

    for _ in range(max_iteraciones):
        # Asignar cada punto al centroide más cercano
        nuevas_etiquetas = []
        for punto in datos:
            distancias = [distancia_euclidiana(punto, c) for c in centroides]
            nuevas_etiquetas.append(distancias.index(min(distancias)))

        # Verificar convergencia
        if nuevas_etiquetas == etiquetas:
            break
        etiquetas = nuevas_etiquetas

        # Recalcular centroides
        for i in range(k):
            puntos_cluster = [datos[j] for j in range(len(datos)) if etiquetas[j] == i]
            if puntos_cluster:
                centroides[i] = calcular_centroide(puntos_cluster)

    return centroides, etiquetas


if __name__ == "__main__":
    # Ejemplo: datos bidimensionales con 3 grupos naturales
    datos = [
        [1.0, 1.0], [1.5, 2.0], [1.0, 1.5],
        [5.0, 5.0], [5.5, 4.5], [5.0, 5.5],
        [9.0, 1.0], [9.5, 1.5], [9.0, 2.0],
    ]

    k = 3
    centroides, etiquetas = kmeans(datos, k)

    print(f"Centroides finales:")
    for i, c in enumerate(centroides):
        print(f"  Cluster {i}: ({c[0]:.2f}, {c[1]:.2f})")

    print(f"\nAsignación de puntos:")
    for i, (punto, etiqueta) in enumerate(zip(datos, etiquetas)):
        print(f"  Punto {punto} -> Cluster {etiqueta}")
