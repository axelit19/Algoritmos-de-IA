"""
Búsqueda en Profundidad (DFS - Depth-First Search)
Recorre un grafo siguiendo cada rama hasta su nodo hoja
antes de retroceder y explorar otra rama.
"""


def dfs(grafo, inicio, objetivo, visitados=None, camino=None):
    """
    Realiza búsqueda en profundidad desde 'inicio' hasta 'objetivo'.

    Args:
        grafo: dict con listas de adyacencia {nodo: [vecinos]}
        inicio: nodo de partida
        objetivo: nodo destino
        visitados: conjunto de nodos ya visitados (uso interno)
        camino: camino actual (uso interno)

    Returns:
        lista con el camino encontrado, o None si no existe
    """
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = []

    visitados.add(inicio)
    camino = camino + [inicio]

    if inicio == objetivo:
        return camino

    for vecino in grafo.get(inicio, []):
        if vecino not in visitados:
            resultado = dfs(grafo, vecino, objetivo, visitados, camino)
            if resultado is not None:
                return resultado

    return None


def dfs_iterativo(grafo, inicio, objetivo):
    """
    Versión iterativa de DFS usando una pila explícita.

    Args:
        grafo: dict con listas de adyacencia {nodo: [vecinos]}
        inicio: nodo de partida
        objetivo: nodo destino

    Returns:
        lista con el camino encontrado, o None si no existe
    """
    pila = [[inicio]]
    visitados = set()

    while pila:
        camino = pila.pop()
        nodo_actual = camino[-1]

        if nodo_actual == objetivo:
            return camino

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            for vecino in grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    pila.append(camino + [vecino])

    return None


if __name__ == "__main__":
    # Ejemplo de uso
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
    }

    inicio = 'A'
    objetivo = 'F'

    camino_recursivo = dfs(grafo, inicio, objetivo)
    print(f"DFS recursivo de {inicio} a {objetivo}: {camino_recursivo}")

    camino_iterativo = dfs_iterativo(grafo, inicio, objetivo)
    print(f"DFS iterativo de {inicio} a {objetivo}: {camino_iterativo}")
