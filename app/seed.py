import random
from itertools import product

from app.models import User, Tovar, Address, Categories
from app.main import db
from faker import Faker

fake = Faker('ru_RU')

def seeds():
    data = User(name="Vasiliy", is_active=True, email='vas@google.com', phone_number='+79997771122')
    data.set_password('111')
    db.session.add(data)
    db.session.commit()



    db.session.refresh(data)

    addr = Address(city='Kazan', ulica='Lenina', user_id=data.id)
    db.session.add(addr)

    db.session.commit()

    categ = Categories(product_type='Одежда', appointment='спортивная', brand='NIKE')
    db.session.add(categ)
    db.session.commit()


    data4 = Tovar(name="Костюм", price=50, ostatok=20, category=categ, url_photo="111.jpg")
    data5 = Tovar(name="Брюки", price=150, ostatok=14, category=categ, url_photo="111.jpg")
    data6 = Tovar(name="Рубашка", price=250, ostatok=10, category=categ, url_photo="111.jpg")

    db.session.add(data4)
    db.session.add(data5)
    db.session.add(data6)
    db.session.commit()


def seed_user():
    for i in range(300):
        categories = ["Одежда", "Обувь", "Прочее"]
        appointment = ['Спортивная', 'Ежедневная', 'Парадкая']
        brand = ['NIKE', 'gr', 'ads']
        activ = [True, False]
        name_tovar = ['Рубашка', 'Брюки', 'Пиджак', 'Ботинки', 'Тубли', 'Запонки']


        user = User(name=fake.first_name_female(), is_active=random.choice(activ), email=fake.email(), phone_number=fake.phone_number())
        user.set_password(fake.password())
        db.session.add(user)


        addr2 = Address(city=fake.city(), ulica=fake.street_name())
        db.session.add(addr2)


        categ = Categories(product_type=random.choice(categories), appointment=random.choice(appointment), brand=random.choice(brand))
        db.session.add(categ)
        db.session.commit()

        tovar = Tovar(name=random.choice(name_tovar), price=random.randint(1, 10000), ostatok = random.randint(1, 1000), url_photo="111.jpg")
        # tovar2 = Tovar(category = C)
        db.session.add(tovar)
        db.session.commit()


        db.session.commit()
        db.session.refresh(user)