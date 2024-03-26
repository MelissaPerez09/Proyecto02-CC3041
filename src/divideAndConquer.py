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
    - Modificado el 23.03.2024
'''

import GraphsReader

#Se lee el archivo con los grafos
reader = GraphsReader.GraphsReader('./files/graphs.txt')
reader.readFile()
graphsList = reader.getGraphsList()

#Se imprimen los grafos
for graph in graphsList:
    print(graph)