from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import DatabaseConfig

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DatabaseConfig)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    # 블루프린트
    from controller import main_views, predictController
    app.register_blueprint(main_views.bp)
    app.register_blueprint(predictController.bp)

    return app

app = create_app()
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)