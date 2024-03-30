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
import time

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
        start_time = time.time()  # Se registra el tiempo de inicio
        shortest_path, shortest_distance = self.divide_and_conquer(start, end, [start], 0)
        end_time = time.time()  # Se registra el tiempo de fin
        execution_time = end_time - start_time  # Se calcula el tiempo de ejecución
        return shortest_path, shortest_distance, execution_time

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

# Lista para almacenar los tiempos de ejecución de cada grafo
execution_times = []

# Se recorren los grafos y se encuentra el camino más corto
for idx, graph_data in enumerate(graphsList, start=1):
    graph = GraphDaC(graph_data)
    print(f"\nGrafo {idx}:")
    path, total_weight, execution_time = graph.shortest_path('s', 't')
    execution_time_ms = execution_time * 1000
    execution_times.append(execution_time_ms)
    if path:
        print("El camino más corto es:", " -> ".join(path), "con un peso total de:", total_weight)
        print(f"Tiempo de ejecución: {execution_time_ms:.5} milisegundos")
    else:
        print("No se encontró un camino.")
        print(f"Tiempo de ejecución: {execution_time_ms:.5} milisegundos")
