from flask import render_template
from . import db
from .models import ReferentielFonds, ReferentielInstruments, Positions, Transactions


def register_routes(app):
    @app.route("/")
    def index():
        """
        Route principale de l'application. Affiche un message de bienvenue.
        """
        return render_template("index.html")

    @app.route("/fonds")
    def voir_fonds():
        """
        Route pour afficher la liste des fonds.

        :return: Rendu du modèle 'fonds.html' avec la liste des fonds.
        """
        fonds = ReferentielFonds.query.all()
        return render_template("fonds.html", fonds=fonds)

    @app.route("/instruments")
    def voir_instruments():
        """
        Route pour afficher la liste des instruments financiers.

        :return: Rendu du modèle 'instruments.html' avec la liste des instruments.
        """
        instruments = ReferentielInstruments.query.all()
        return render_template("instruments.html", instruments=instruments)

    @app.route("/positions/<int:fond_id>")
    def voir_positions(fond_id):
        """
        Route pour afficher les positions d'un fonds spécifique.

        :param fond_id: ID du fonds dont les positions doivent être affichées.
        :return: Rendu du modèle 'positions.html' avec la liste des positions pour le fonds spécifié.
        """
        positions = Positions.query.filter_by(fond_id=fond_id).all()
       
        return render_template("positions.html", positions=positions)

    @app.route("/positions/<int:position_id>/historique")
    def transaction_historique(position_id):
        """
        Affiche l'historique des transactions pour une position donnée.

        Paramètres:
            position_id (int): L'identifiant de la position dont on souhaite voir l'historique des transactions.

        Retourne:
            render_template: Le template HTML 'transaction_historique.html' avec les données de la position
                            et les transactions associées.
        """
        # Récupère la position spécifique par son ID. Si la position n'existe pas, renvoie une erreur 404.
        position = Positions.query.get_or_404(position_id)

        # Récupère toutes les transactions associées à cette position.
        transactions = Transactions.query.filter_by(position_id=position_id).all()

        # Rendu du template HTML avec les données de la position et les transactions associées.
        return render_template(
            "transaction_historique.html", position=position, transactions=transactions
        )
