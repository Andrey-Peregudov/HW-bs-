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

    activ = [True, False]

    for i in range(300):
        try:
            data2 = User(name=fake.first_name_female(), is_active=random.choice(activ), email=fake.email(), phone_number=fake.phone_number())
            data2.set_password(fake.password())
            db.session.add(data2)

        except Exception as e:
            print(f"Ошибка при создании пользователя {i+1}: {e}")
            # Важно: Обработать ошибку, чтобы не остановить выполнение!
            continue  # Переходим к следующей итерации цикла
    db.session.commit(data2)
    db.session.refresh(data)

    db.session.refresh(data)

    addr = Address(city='Kazan', ulica='Lenina', user_id=data.id)
    db.session.add(addr)

    for i in range(300):
        addr2 = Address(city=fake.city(), ulica=fake.street_name(), user_id=data.id)
        db.session.add(addr2)

    db.session.commit()

    categ = Categories(product_type='Одежда', appointment='спортивная', brand='NIKE')
    db.session.add(categ)
    db.session.commit()
    for i in range(300):
        categ2 = Categories(product_type=fake.text(max_nb_chars=50), appointment=fake.text(max_nb_chars=50), brand=fake.company())
        db.session.add(categ2)
        db.session.commit()


    categories = ["Одежда", "Обувь", "Прочее"]


    data4 = Tovar(name="Костюм", price=50, ostatok=20, category=categ, url_photo="111.jpg")
    data5 = Tovar(name="Брюки", price=150, ostatok=14, category=categ, url_photo="111.jpg")
    data6 = Tovar(name="Рубашка", price=250, ostatok=10, category=categ, url_photo="111.jpg")
    for i in range(300):
        data7 = Tovar(name=fake.text(max_nb_chars=30), price=random.randint(1,1000), ostatok=random.randint(1,100), category=random.choice(categories), url_photo="111.jpg")
        db.session.add(data7)
        db.session.commit()
    db.session.add(data4)
    db.session.add(data5)
    db.session.add(data6)
    db.session.commit()



