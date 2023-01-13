from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from config import DatabaseConfig


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    CORS(app, supports_credentials=True, origins="localhost:3000")
    app.config.from_object(DatabaseConfig)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    # API Swagger
    api = Api(
        app,
        version='v1',
        title="Silicon Project's API Server",
        description="Dessert API Server",
        terms_url="/",
        contact="junsu1222@naver.com",
        license="MIT",
    )
    from controller import listController
    api.add_namespace(listController.Products, '/')

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)



