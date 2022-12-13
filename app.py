from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

abs_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] =   "sqlite:///" + abs_dir + "\\teste.db"

db = SQLAlchemy(app)

from models import *

def connection():
    with app.app_context():
        db.create_all() 

Migrate(app, db)

from views import *

if __name__ == "__main__":
    app.run()