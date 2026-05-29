from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'DAwdasdWaDSADWA5d5a4d8ad4adawdasshdgnykvmul9oipoiyr56344252d'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from appInvest.views import homepage
from appInvest.models import Investor

login_manager = LoginManager(app)

login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return Investor.query.get(int(user_id))

with app.app_context():
    db.create_all()