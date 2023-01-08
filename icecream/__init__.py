from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from icecream.config.DatabaseConfig import getURI

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = getURI()
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)
# from entity import product
db.create_all()

if __name__ == '__main__':
    app.run()
