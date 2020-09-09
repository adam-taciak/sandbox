from flask import Flask
from flask_cors import CORS

from peewee import SqliteDatabase

from schema import schema

app = Flask(__name__)
app.config.from_object('config.Configuration')

CORS(app)

db = SqliteDatabase('baza-strony.db', check_same_thread=False)


# graphql
from flask_graphql import GraphQLView
app.add_url_rule('/api', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


