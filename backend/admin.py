from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView

from app import app
from models import Page, Post

class PageAdmin(ModelView):
    pass

class PostAdmin(ModelView):
    pass


admin = Admin(app, name='Administration panel', template_mode='bootstrap3')
admin.add_view(PageAdmin(Page, 'Pages'))
admin.add_view(PostAdmin(Post, 'Posts'))
