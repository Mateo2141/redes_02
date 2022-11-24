import config
from DISClib.ADT import graph as gr
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Graphs import scc
from DISClib.Utils import error as error
assert config


# -----------------------------------------------------
#                       API
# -----------------------------------------------------

def newCatalog ():
    catalog = {
        'grafo_red': None,
        'lista':None
    }
    catalog['grafo_red']= gr.newGraph(datastructure='ADJ_LIST',
                                              directed=False,
                                              size=14000,
                                              comparefunction=comparegraph)
    return catalog



# Funciones para agregar informacion al grafo

def carga (catalog, valor):
    addNodo_origen(catalog, valor["origen"])
    addNodo_destino(catalog, valor["destino"])
    conexion(catalog, valor["origen"], valor["destino"], valor["costo"])
    


def addNodo_origen(catalog, valor):
    try:    
        if not gr.containsVertex(catalog['grafo_red'], valor):
                gr.insertVertex(catalog['grafo_red'], valor)
    except Exception as exp:
        error.reraise(exp, 'model:addNodo_origen')
    return catalog

def addNodo_destino(catalog, valor):
    try:    
        if not gr.containsVertex(catalog['grafo_red'], valor):
                gr.insertVertex(catalog['grafo_red'], valor)
    except Exception as exp:
        error.reraise(exp, 'model:addNodo_origen')
    return catalog

def conexion(catalog, origen, destino, costo):
    edge = gr.getEdge(catalog['grafo_red'], origen, destino)
    if edge is None:
        gr.addEdge(catalog['grafo_red'], origen, destino, costo)
    return catalog


# ==============================
# Algoritmo de Link State
# ==============================

def linkState (catalog, v_ini):
    vertices = gr.vertices(catalog['grafo_red'])
    lista_general = lt.newList(datastructure="ARRAY_LIST", cmpfunction=comparelist)
    lista_fila = lt.newList(datastructure="ARRAY_LIST", cmpfunction=comparelist)
    lt.addLast(lista_fila, "N'")
    for i in lt.iterator(vertices):
        lt.addLast(lista_fila, i)
    lt.addLast(lista_general, lista_fila)
    primer_para = v_ini
    lista_filas = lt.newList(datastructure="ARRAY_LIST", cmpfunction=comparelist)
    lt.addFirst(lista_filas, v_ini)
    for x in range (lt.size(vertices)):
        lt.addLast(lista_filas, 909)
    for i in range(lt.size(vertices)): 
        lista_metros = lt.newList(datastructure="ARRAY_LIST", cmpfunction=comparelist)
        nueva = lt.subList(lista_filas, 1, lt.size(lista_fila)) 
        lt.changeInfo(nueva, 1, primer_para)
        vecinos = gr.adjacentEdges(catalog['grafo_red'],primer_para)
        vecinos_menores = merge.sort(vecinos, comparelord)
        for j in lt.iterator(vecinos):
            presente = lt.isPresent(lista_metros,j["vertexB"])
            if presente == 0:
                destino = j ["vertexB"]
                peso = int(j ["weight"])
                posicion = lt.isPresent(lista_fila,destino)
                if posicion != 0:
                    if peso < lt.getElement(nueva, posicion):
                        tupla = (peso, destino)
                        cambio_ele = lt.changeInfo(nueva, posicion, tupla)
        lt.addLast(lista_general, nueva)
        c = lt.getElement(vecinos_menores, 1)
        primer_para = c["vertexB"]
        lt.addLast(lista_metros, primer_para)            
    return lista_general

# ==============================
# Funciones de Ordenamiento
# ==============================

def primerosultimostres (valor):
    tamaño = lt.size(valor)
    if tamaño >= 6:
        primeros = lt.subList(valor,1,3)
        ultimos = lt.subList(valor,tamaño-2,3)
        l_final = lt.newList('ARRAY_LIST')
        for i in lt.iterator(primeros):
            lt.addLast(l_final, i)
        for j in lt.iterator(ultimos):
            lt.addLast(l_final, j)
    else:
        l_final = valor
    return l_final
   

def comparelord (arco1, arco2):
    mayor = False
    arco1 = arco1['weight'] 
    arco2 = arco2['weight'] 
    if arco1 < arco2:
        mayor = True
    return  mayor



# ==============================
# Funciones de Comparacion
# ==============================


def comparegraph (nodo1, nodo2):
    nodo2 = nodo2['key']
    if (nodo1 == nodo2):
        return 0
    elif (nodo1 > nodo2):
        return 1
    else:
        return -1


def comparelist (nodo1, nodo2):
    if (nodo1 == nodo2):
        return 0
    elif (nodo1 > nodo2):
        return 1
    else:
        return -1