"""
Algoritmo A* (A Estrella)
Algoritmo de búsqueda heurística que encuentra el camino óptimo
usando f(n) = g(n) + h(n), donde g(n) es el costo acumulado
y h(n) es la heurística (estimación al objetivo).
"""
import heapq


def a_estrella(grafo, inicio, objetivo, heuristica):
    """
    Realiza búsqueda A* desde 'inicio' hasta 'objetivo'.

    Args:
        grafo: dict con costos {nodo: [(vecino, costo), ...]}
        inicio: nodo de partida
        objetivo: nodo destino
        heuristica: función h(nodo, objetivo) -> float

    Returns:
        (camino, costo_total) o (None, inf) si no existe camino
    """
    # (f, g, nodo, camino)
    cola_prioridad = [(heuristica(inicio, objetivo), 0, inicio, [inicio])]
    visitados = {}

    while cola_prioridad:
        f, g, nodo_actual, camino = heapq.heappop(cola_prioridad)

        if nodo_actual == objetivo:
            return camino, g

        if nodo_actual in visitados and visitados[nodo_actual] <= g:
            continue
        visitados[nodo_actual] = g

        for vecino, costo in grafo.get(nodo_actual, []):
            g_nuevo = g + costo
            if vecino not in visitados or visitados[vecino] > g_nuevo:
                f_nuevo = g_nuevo + heuristica(vecino, objetivo)
                heapq.heappush(cola_prioridad, (f_nuevo, g_nuevo, vecino, camino + [vecino]))

    return None, float('inf')


if __name__ == "__main__":
    # Ejemplo: grafo con coordenadas en un plano 2D
    # Los nodos son letras con posiciones (x, y)
    posiciones = {
        'A': (0, 0),
        'B': (1, 2),
        'C': (2, 0),
        'D': (3, 2),
        'E': (4, 0),
    }

    grafo = {
        'A': [('B', 2.24), ('C', 2.0)],
        'B': [('A', 2.24), ('D', 2.24), ('C', 2.24)],
        'C': [('A', 2.0), ('B', 2.24), ('E', 2.0)],
        'D': [('B', 2.24), ('E', 2.24)],
        'E': [('C', 2.0), ('D', 2.24)],
    }

    def heuristica_euclidiana(nodo, objetivo):
        x1, y1 = posiciones[nodo]
        x2, y2 = posiciones[objetivo]
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    inicio = 'A'
    objetivo = 'E'
    camino, costo = a_estrella(grafo, inicio, objetivo, heuristica_euclidiana)
    print(f"Camino A* de {inicio} a {objetivo}: {camino}")
    print(f"Costo total: {costo:.2f}")
