"""
Búsqueda en Anchura (BFS - Breadth-First Search)
Recorre un grafo nivel por nivel, garantizando encontrar
el camino más corto en grafos no ponderados.
"""
from collections import deque


def bfs(grafo, inicio, objetivo):
    """
    Realiza búsqueda en anchura desde 'inicio' hasta 'objetivo'.

    Args:
        grafo: dict con listas de adyacencia {nodo: [vecinos]}
        inicio: nodo de partida
        objetivo: nodo destino

    Returns:
        lista con el camino encontrado, o None si no existe
    """
    if inicio == objetivo:
        return [inicio]

    visitados = {inicio}
    cola = deque([[inicio]])

    while cola:
        camino = cola.popleft()
        nodo_actual = camino[-1]

        for vecino in grafo.get(nodo_actual, []):
            if vecino == objetivo:
                return camino + [vecino]
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(camino + [vecino])

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
    camino = bfs(grafo, inicio, objetivo)
    print(f"Camino de {inicio} a {objetivo}: {camino}")
