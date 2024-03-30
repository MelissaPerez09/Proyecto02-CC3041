'''
 * Nombre: dynamicProgramming.py
 * Autoras:
   - Melissa Pérez, 21385
   - Fernanda Esquivel, 21542
 * Descripción: Encuentra el camino más corto dentro de un grafo ponderado utilizando programación dinámica.
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
   - Creado el 23.03.2024
   - Modificado el 30.03.2024
'''

import GraphsReader
import time

"""
Función que lee los grafos del archivo de texto
* return: Lista de grafos
"""
def readFile():
   #Se lee el archivo con los grafos
   reader = GraphsReader.GraphsReader('./files/graphs.txt')
   reader.readFile()
   graphsList = reader.getGraphsList()

   return graphsList

"""
Función que encuentra el camino más corto entre dos vértices en un grafo ponderado utilizando programación dinámica
* graph: Grafo
* start: Nodo de inicio
* end: Nodo final
* return: Peso del camino más corto
"""
def shortestPathAlgorithm(graph, start, end):
   # Convertir la lista de tuplas en un diccionario de diccionarios para el grafo
   graph_dict = {}
   for node, edges in graph.items():
      graph_dict[node] = {neighbor: weight for neighbor, weight in edges}

   # Asegurarse de que todos los nodos estén en el diccionario, incluido el nodo final
   all_nodes = set(graph_dict.keys()) | {end} | {n for edges in graph.values() for n, _ in edges}
   dp = {node: float('inf') for node in all_nodes}
   dp[start] = 0

   # Lista para procesar los nodos
   for _ in range(len(all_nodes)):
      for node in all_nodes:
         if node in graph_dict:
            for neighbor, weight in graph_dict[node].items():
               if dp[node] + weight < dp[neighbor]:
                  dp[neighbor] = dp[node] + weight

   if dp[end] == float('inf'):
      return None  # Devolver None si no hay camino
   else:
      return dp[end]

"""
Función que evalúa los grafos y devuelve una lista con los tiempos de ejecución y el peso del camino más corto
* graphsList: Lista de grafos
* start: Nodo de inicio
* end: Nodo final
* return: Lista con los tiempos de ejecución y el peso del camino más corto
"""
def evaluateGraphs(graphsList, start, end):
   results = []

   for graph in graphsList:
      timeStart = time.time()
      pathWeight = shortestPathAlgorithm(graph, start, end)
      timeEnd = time.time()
      ejecutionTime = timeEnd - timeStart
      results.append([ejecutionTime, pathWeight])

   return results

#Prueba de ejecución
graphsList = readFile()
results = evaluateGraphs(graphsList, 's', 't')
print(results)
