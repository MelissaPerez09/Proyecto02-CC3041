'''
 * Nombre: divideAndConquer.py
 * Autoras:
    - Melissa Pérez, 21385
    - Fernanda Esquivel, 21542
 * Descripción: Encuentra el camino más corto dentro de un grafo ponderado utilizando divide and conquer.
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Creado el 23.03.2024
    - Modificado el 28.03.2024
'''

import GraphsReader

#Se lee el archivo con los grafos
reader = GraphsReader.GraphsReader('./files/graphs.txt')
reader.readFile()
graphsList = reader.getGraphsList()

class GraphDaC:
    def __init__(self, graph_data):
        self.graph = graph_data

    """
    Método que encuentra el camino más corto entre dos vértices en un grafo ponderado.
    """
    def shortest_path(self, start, end):
        shortest_path, shortest_distance = self.divide_and_conquer(start, end, [start], 0)
        return shortest_path, shortest_distance

    """
    Método que aplica el paradigma de divide y conquista para encontrar el camino más corto.
    """
    def divide_and_conquer(self, current, end, path, total_weight):
        if current == end:
            return path, total_weight

        shortest_path = None
        shortest_distance = float('inf')
        
        # Búsqueda recursiva de los caminos hacia el vértice final
        # En cada paso elige el nodo que minimiza la distancia total
        for next_vertex, weight in self.graph.get(current, []):
            if next_vertex not in path:
                new_path, new_distance = self.divide_and_conquer(next_vertex, end, path + [next_vertex], total_weight + weight)
                if new_path and new_distance < shortest_distance:
                    shortest_path = new_path
                    shortest_distance = new_distance

        return shortest_path, shortest_distance

# Se recorren los grafos y se encuentra el camino más corto
for idx, graph_data in enumerate(graphsList, start=1):
    graph = GraphDaC(graph_data)
    print(f"\nGrafo {idx}:")
    path, total_weight = graph.shortest_path('s', 't')
    if path:
        print("El camino más corto es:", " -> ".join(path), "con un peso total de:", total_weight)
    else:
        print("No se encontró un camino.")
