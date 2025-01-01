from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from database import Config

app = Flask(__name__, static_folder='static', template_folder='templates')

app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = '/app/static'

db = SQLAlchemy(app)

from models import Post

with app.app_context():
    db.create_all()
    # from seeds import seed_fake
    # seed_fake()


@app.route('/tovar')
@app.route('/tovar/<offset>')
def index(offset=10):
    # desc() - с конца списка
    # limit() - количество записей
    # offset() - количество пропусков
    # order_by() - сортировка
    posts = Post.query.order_by(Post.name).limit(10).offset(offset).all()
    print(len(posts))
    return render_template('index.html', posts=posts, offset=offset)


@app.route('/jennifer')
def jennifer():
    posts = Post.query.where(Post.name == 'Jennifer').where(Post.email == 'achurch@example.org').order_by(
        Post.email).all()
    dlinna = len(posts)
    for post in posts:
        print(post.name, post.email)
    return {'ok': dlinna}


if __name__ == '__main__':
    app.run(port=5002, debug=True)
