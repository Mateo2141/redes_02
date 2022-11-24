import csv
import config as cf
import Modelo_Algoritmo as model

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def newController():
    control = {
        'model':None
    }
    control['model'] = model.newCatalog()
    return control


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


def cargar_datos(catalog):
    direccion = cf.data_dir + "vuelos.csv"
    input_file = csv.DictReader(open(direccion, encoding="utf-8"),
                                delimiter=",")
    for nodo in input_file:
        model.carga(catalog, nodo)

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def linkState (catalog, v_ini):
    return model.linkState (catalog, v_ini)

def primerosultimostres (valor):
    return model.primerosultimostres (valor)
