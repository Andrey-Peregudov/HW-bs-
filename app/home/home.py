from flask import Blueprint, render_template, flash
from flask_login import current_user, login_user, logout_user
from ..beautifulsoup.main import get_curs


from app.models import Tovar
from app.main import korzina

home_bp = Blueprint('home', __name__, template_folder='templates', static_folder='static')


@home_bp.route('/')
@home_bp.route('/index')
def index():
    korzin = korzina()
    tovar = Tovar.query.all()
    kolvo = len(korzin)
    flash(get_curs())

    return render_template('home/index.html', tovars=tovar, korzina=kolvo)
