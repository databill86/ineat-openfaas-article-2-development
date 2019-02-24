import graphene
from graphene_mongo import MongoengineObjectType
from models import Movie as MovieModel

class Movie(MongoengineObjectType):
    class Meta:
        model = MovieModel

class Query(graphene.ObjectType):
    movies = graphene.List(Movie)
    def resolve_movies(self, info):
    	return list(MovieModel.objects.all())

schema = graphene.Schema(query=Query)