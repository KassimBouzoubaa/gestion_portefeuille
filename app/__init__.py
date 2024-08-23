from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from . import routes, models

        routes.register_routes(app)  # Enregistrer les routes
        db.create_all()  # Créer les tables si elles n'existent pas encore
        print("Base de données initialisée avec succès !")

        try:
            from .insert_data import populate_db

            populate_db()
        except Exception as e:
            print(f"Erreur lors du peuplement de la base de données : {e}")

    return app
