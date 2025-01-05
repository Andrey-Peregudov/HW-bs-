from flask import Blueprint, render_template
from app.models import Categories, Tovar
from app.main import db
from app.main import korzina

catalog_bp = Blueprint('catalog', __name__, template_folder='templates', static_folder='static')


@catalog_bp.route('/catalog')
@catalog_bp.route('/catalog/<int:offset>')
def catalog(offset=10):

    categories = db.session.query(Categories.product_type).order_by(Categories.product_type).distinct()

    tovars = Tovar.query.order_by(Tovar.name).limit(10).offset(offset).all()

    return render_template('catalog.html', categories=categories, tovars=tovars, offset=offset)

