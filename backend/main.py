from app import app

from admin import *
from views import *
from models import *

if __name__ == '__main__':
    Page.create_table()
    Post.create_table()
    app.run(host = '0.0.0.0', port = 3000)
