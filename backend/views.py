import json

from app import app
from models import Post, Page

from playhouse.shortcuts import model_to_dict, dict_to_model

@app.route('/')
def index():
    return 'home'

@app.route('/post/<slug>')
def post(slug):
    post = Post().select().where(Post.slug == slug).get()

    print(post)

    json_data = json.dumps(model_to_dict(post), indent=4, sort_keys=True, default=str)

    return json_data
