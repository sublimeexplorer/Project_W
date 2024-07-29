from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy() # Subject to change (depending on what database is decided on)

def create_app():
    app = Flask(__name__) # init Flask instance
    app.config.from_object(Config)

    db.init_app(app)

    from .routes import main_routes, user_routes
    app.register_blueprint(main_routes.bp)
    app.register_blueprint(user_routes.bp)

    return app