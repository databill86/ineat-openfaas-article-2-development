from pymongo import MongoClient
import json

def handle(req):
    movie = json.loads(req)

    client = MongoClient('mongodb://192.168.1.19:27017')

    movies = db.movies
    result = movies.insert_one(movie)

    return "Movie created : " + result.inserted_id
