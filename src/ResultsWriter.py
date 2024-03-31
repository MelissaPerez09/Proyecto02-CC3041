'''
 * Nombre: ResultsWriter.py
 * Autoras:
    - Melissa Pérez, 21385
    - Fernanda Esquivel, 21542
 * Descripción: Lee los resultados de los algoritmos y los escribe en un archivo de Excel.
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Creado el 30.03.2024
    - Modificado el 30.03.2024
'''

import pandas as pd

'''
Clase que escribe los resultados de los algoritmos en un archivo de Excel
'''
class ResultsWriter:
    '''
    Constructor de la clase
    '''
    def __init__(self, times, graphs, filename):
        self.times = times
        self.graphs = graphs
        self.filename = filename

    '''
    Método que escribirá los resultados en un archivo de Excel
    '''
    def writeResults(self):
        print("\nEscribiendo resultados en el archivo Excel...")
        #Preparamos los datos para el DataFrame
        data = {
            'Nodos': [],
            'Aristas': [],
            'Tiempo': self.times 
        }

        for graph in self.graphs:
            #Obtenemos los nodos y aristas del grafo
            nodos = list(graph.keys())
            aristas = [arista for destinos in graph.values() for arista in destinos]

            data['Nodos'].append(len(nodos))
            data['Aristas'].append(len(aristas))

        #Creamos un DataFrame con los datos
        df = pd.DataFrame(data)

        #Escribimos el DataFrame a un archivo Excel
        df.to_excel(self.filename, index=False)

# Ejemplo de uso
# times = [0.0, 0.0]
# graphs = [{'s': [('A', 1)], 'A': [('B', 2)], 'B': [('C', 3)], 'C': [('t', 4)], 't': []}, {'s': [('A', 1)], 'A': [('B', 2)], 'B': [('C', 3)], 'C': [], 't': []}]
# writer = ResultsWriter(times, graphs, 'resultados.xlsx')
# writer.writeResults()