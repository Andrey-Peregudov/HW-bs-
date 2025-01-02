
from models import Post
from app import db
from faker import Faker

fake = Faker()


def seed_fake():
    for i in range(2000):
        data = Post(name=fake.first_name_female(), news=fake.text(max_nb_chars=1000), email=fake.email())
        db.session.add(data)
        db.session.commit()
