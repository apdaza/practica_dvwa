import pymongo
from bson import ObjectId

HOST = "127.0.0.1"
PORT = 27017
DATABASE = "personasdb"
COLLECTION = "personas"
URI_CONECTION = "mongodb://{}:{}/".format(HOST, PORT)

def consultar(id=None):
    data = {}
    try:
        cliente = pymongo.MongoClient(URI_CONECTION)
        coleccion = cliente[DATABASE][COLLECTION]
        if id is None:
            condicion = {}
            resultado = coleccion.find(condicion)
        else:
            condicion = {"_id": ObjectId(id)}
            resultado = coleccion.find_one(condicion)
        data = resultado
    except Exception as e:
        print("Error: {}".format(e))
    finally:
        return data

def insertar(data):    
    try:
        cliente = pymongo.MongoClient(URI_CONECTION)
        coleccion = cliente[DATABASE][COLLECTION]
        coleccion.insert_one(data)
    except Exception as e:
        print("Error: {}".format(e))

def actualizar(id, data):
    try:
        cliente = pymongo.MongoClient(URI_CONECTION)
        coleccion = cliente[DATABASE][COLLECTION]
        condicion = {"_id": ObjectId(id)}
        coleccion.update_one(condicion, {"$set": data})
    except Exception as e:
        print("Error: {}".format(e))   

def borrar(id):
    try:
        cliente = pymongo.MongoClient(URI_CONECTION)
        coleccion = cliente[DATABASE][COLLECTION]
        condicion = {"_id": ObjectId(id)}
        coleccion.delete_one(condicion)
    except Exception as e:
        print("Error: {}".format(e))
