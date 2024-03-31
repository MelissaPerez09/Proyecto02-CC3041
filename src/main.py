'''
 * Nombre: main.py
 * Autoras:
    - Melissa Pérez, 21385
    - Fernanda Esquivel, 21542
 * Descripción: Programa principal que ejecuta los algoritmos de divide and conquer y programación dinámica para encontrar el camino más corto en un grafo ponderado.
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Creado el 30.03.2024
    - Modificado el 30.03.2024
'''

import DynamicProgramming
import ResultsWriter
import GraphsReader
from DivideAndConquer import execute_algorithm

"""
Función principal que ejecuta el programa
"""
def main():
    #Se lee el archivo con los grafos
    reader = GraphsReader.GraphsReader('./files/graphs.txt')
    reader.readFile()
    graphsArray = reader.getGraphsList()

    while True:
        print("\nMenú:")
        print("1. Obtener camino más corto con Divide and Conquer")
        print("2. Obtener camino más corto con Programación Dinámica")
        print("3. Salir del programa")
        
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == "1":
            dacTimes = execute_algorithm()
            writerDAC = ResultsWriter.ResultsWriter(dacTimes, graphsArray, 'DaC.xlsx')
            writerDAC.writeResults()
        elif opcion == "2":
            dp = DynamicProgramming.DynamicProgramming()
            dp.executeAlgorithm()
            dpTimes = dp.getExecutionTimes()
            writerDP = ResultsWriter.ResultsWriter(dpTimes, graphsArray, 'DP.xlsx')
            writerDP.writeResults()
        elif opcion == "3":
            print("¡Gracias por utilizar nuestro programa!")
            break
        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

if __name__ == "__main__":
    main()