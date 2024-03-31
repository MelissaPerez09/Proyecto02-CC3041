'''
 * Nombre: GraphsReader.py
 * Autoras:
    - Melissa Pérez, 21385
    - Fernanda Esquivel, 21542
 * Descripción: Lee el archivo txt con los grafos y los guarda en una lista.
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Creado el 23.03.2024
    - Modificado el 23.03.2024
'''

'''
Clase que lee el archivo con los grafos y los guarda en una lista
'''
class GraphsReader:
    '''
    Constructor de la clase
    '''
    def __init__(self, file):
        self.file = file
        self.graphsList = []

    '''
    Método que lee el archivo con los grafos y los guarda en una lista
    '''
    def readFile(self):
        with open(self.file, 'r') as graphFile:
            for line in graphFile:
                graph = eval(line)
                self.graphsList.append(graph)

    '''
    Método que imprime los grafos
    '''
    def printGraphs(self):
        for graph in self.graphsList:
            print(graph)
    
    '''
    Método que regresa la lista de grafos
    '''
    def getGraphsList(self):
        return self.graphsList


# Ejemplo de uso
# reader = GraphsReader('./files/graphs.txt')
# reader.readFile()
# print(reader.getGraphsList())