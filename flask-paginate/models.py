import json

import sqlalchemy as sa
from app import db


class Post(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    news = sa.Column(sa.String(2000))
    name = sa.Column(sa.String(255))
    email = sa.Column(sa.String(255))



