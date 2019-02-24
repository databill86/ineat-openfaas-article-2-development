from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (EmbeddedDocumentField, ListField, StringField)

class Person(EmbeddedDocument):
    firstname = StringField()
    lastname = StringField()

class Movie(Document):
    meta = {'collection': 'movies'}
    title = StringField()
    type = StringField()
    year = StringField()
    director = EmbeddedDocumentField(Person)
    actors = ListField(EmbeddedDocumentField(Person))