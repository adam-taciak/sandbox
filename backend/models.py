import datetime

from app import db
from peewee import *

class BaseModel(Model):
    class Meta:
        database = db

class Post(BaseModel):
    title = CharField()
    slug = CharField(unique=True)
    content = TextField()
    create_date = DateTimeField(default=datetime.datetime.now)
    edit_date = DateTimeField()
    published = BooleanField()

class Page(BaseModel):
    title = CharField()
    slug = CharField(unique=True)
    content = TextField()
    create_date = DateTimeField()
    edit_date = DateTimeField(default=datetime.datetime.now)
    published = BooleanField()

