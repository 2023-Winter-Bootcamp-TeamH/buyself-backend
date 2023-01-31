from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics
from config import DatabaseConfig
import logging

db = SQLAlchemy()
migrate = Migrate()
app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logging.info("Setting LOGLEVEL to INFO")

metrics = PrometheusMetrics(app)
metrics.info("app_info", "App Info, this can be anything you want", version="1.0.3")


def create_app():

    app.config['JSON_AS_ASCII'] = False
    app.config.from_object(DatabaseConfig)

    # CORS
    CORS(app, resources={r'*': {'origins': '*'}})

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

    from controller import searchController,listController,predictController, paymentController
    api.add_namespace(searchController.Products, '/')
    api.add_namespace(listController.Products, '/')
    api.add_namespace(predictController.Products, '/')
    api.add_namespace(paymentController.Products, '/')

    return app



