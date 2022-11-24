import controller_algoritmo as controller 
from tabulate import tabulate
import sys
from DISClib.ADT import list as lt

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información en el grafo")
    print("3- Camino de menor costo")
    print("4- Tabla de costos")
    print("0- Salir")
    print("*******************************************")


    

"""
Menu principal
"""



while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        catalog = controller.newController()

    elif int(inputs[0]) == 2:
        print ("Cargando información en el grafo")
        controller.cargar_datos(catalog['model'])

    elif int(inputs[0]) == 3:
        origen = input("¿cuál es el origen que deseas buscar?")
        respuesta =controller.linkState(catalog['model'], origen)
        pri = controller.primerosultimostres(respuesta)
        i = 1
        lista = []
        while i <= lt.size(pri):
            j=1
            valor = lt.getElement(pri,i)
            sublista = []
            while j <= lt.size(valor):   
                elemento = lt.getElement(valor,j)
                sublista.append(elemento)
                j+=1
            lista.append(sublista)
            i += 1
        print(tabulate(lista, tablefmt='fancy_grid'))
        
    elif int(inputs[0]) == 4:
        origen = input("¿cuál es el origen que deseas buscar?")
        respuesta =controller.linkState(catalog['model'], origen)
        pri = controller.primerosultimostres(respuesta)
        i = 1
        lista = []
        while i <= lt.size(pri):
            j=1
            valor = lt.getElement(pri,i)
            sublista = []
            while j <= lt.size(valor):   
                elemento = lt.getElement(valor,j)
                sublista.append(elemento)
                j+=1
            lista.append(sublista)
            i += 1
        print(tabulate(lista, tablefmt='fancy_grid'))

    else:
        sys.exit(0)
sys.exit(0)