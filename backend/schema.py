import graphene
from graphene import ObjectType, Boolean, String, Field, Schema
#from models import Post as PostModel, Page as PageModel

class Post(ObjectType):
    title = String()
    content = String()
    published = Boolean()

class Page(ObjectType):
    title = String()
    content = String()
    published = Boolean()


class Query(ObjectType):
    posts = graphene.List(Post)
    pages = graphene.List(Page)

    post = graphene.Field(Post)
    page = graphene.Field(Page)

    def resolve_posts(parent, info):
        posts = list()
        posts.append(Post(title='first post', content='content', published=True))
        posts.append(Post(title='second post', content='content', published=False))
        posts.append(Post(title='third post', content='content', published=True))
        return posts

    def resolve_pages(parent, info):
        return list()

    def resolve_post(parent, info, slug):
        return Post()

    def resolve_page(parent, info, slug):
        return Page()


schema = Schema(query=Query)
