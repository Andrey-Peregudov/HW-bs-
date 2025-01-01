import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # POSTS_PER_PAGE = 30

    SECRET_KEY = 'secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
         'sqlite:///' + os.path.join(basedir, 'flask_pag.db')

