'''
 * Nombre: DynamicProgramming.py
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
   #Convertir la lista de tuplas en un diccionario de diccionarios para el grafo
   graphDict = {}
   for node, edges in graph.items():
      graphDict[node] = {neighbor: weight for neighbor, weight in edges}

   #Asegurarse de que todos los nodos estén en el diccionario, incluido el nodo final
   allNodes = set(graphDict.keys()) | {end} | {n for edges in graph.values() for n, _ in edges}
   dp = {node: float('inf') for node in allNodes}
   dp[start] = 0

   #Rastrear el nodo previo para reconstruir el camino
   previous = {node: None for node in allNodes}

   #Lista para procesar los nodos
   for _ in range(len(allNodes)):
      for node in allNodes:
            if node in graphDict:
               for neighbor, weight in graphDict[node].items():
                  if dp[node] + weight < dp[neighbor]:
                     dp[neighbor] = dp[node] + weight
                     previous[neighbor] = node

   #Reconstruir el camino desde el final hasta el inicio
   if dp[end] == float('inf'):
      return None  #Devolver None si no hay camino

   path = []
   currentNode = end
   while currentNode is not None:
      path.append(currentNode)
      currentNode = previous[currentNode]
   path.reverse()

   return (path, dp[end])

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
      pathInfo = shortestPathAlgorithm(graph, start, end)
      timeEnd = time.time()
      ejecutionTime = timeEnd - timeStart
      results.append([pathInfo, ejecutionTime])

   return results

"""
Método que imprime los resultados de los algoritmos
* results: Resultados de los algoritmos
"""
def printResults(results):
   for idx, result in enumerate(results, start=1):
      pathInfo, ejecutionTime = result
      print(f"\nGrafo {idx}:")
      if pathInfo is None:
         print("No se encontró un camino.")
         print(f"Tiempo de ejecución: {ejecutionTime:.5} milisegundos")
      else:
         path, weight = pathInfo
         if path:
            print("El camino más corto es:", " -> ".join(path), "con un peso total de:", weight)
            print(f"Tiempo de ejecución: {ejecutionTime:.5} milisegundos")

"""
Clase que encuentra el camino más corto dentro de un grafo ponderado utilizando programación dinámica
"""
class DynamicProgramming:
   """
   Constructor de la clase
   """
   def __init__(self):
      self.graphsList = readFile()
      
   """
   Método que ejecuta el algoritmo
   """
   def executeAlgorithm(self):
      self.results = evaluateGraphs(self.graphsList, 's', 't')
      printResults(self.results)
      #print(self.results)
      
   """
   Método que devuelve los resultados de los algoritmos
   """
   def getResults(self):
      return self.results
   
   """
   Método que devuelve los resultados de los algoritmos
   """
   def getExecutionTimes(self):
      self.executionTimes = []

      for sub_array in self.results:
         if isinstance(sub_array, list) and len(sub_array) >= 2:
               self.executionTimes.append(sub_array[1])
      
      return self.executionTimes

# Prueba de ejecución
# dp = DynamicProgramming()
# dp.executeAlgorithm()
# print(dp.getExecutionTimes())
