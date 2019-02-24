from pymongo import MongoClient
from schema import Query
import json

def handle(req):
    # Connexion a la base mongo
    connect('moviesDB', host='mongodb://192.168.1.19:27017', alias='default')

    # Extraction de la requête passée en paramètre lors de l'appel
    query = json.loads(req)["query"]
    
    # Exécution de la requête
    result = schema.execute(query)
    
    return result
