from . import db
from .models import ReferentielFonds, ReferentielInstruments, Positions, Transactions
from datetime import datetime


def populate_db():
    try:
        # Exemples de données pour ReferentielFonds
        fonds1 = ReferentielFonds(id=1, nom="Fonds A")
        fonds2 = ReferentielFonds(id=2, nom="Fonds B")
        fonds3 = ReferentielFonds(id=3, nom="Fonds C")
        db.session.add_all([fonds1, fonds2, fonds3])

        # Exemples de données pour ReferentielInstruments
        instrument1 = ReferentielInstruments(
            id=1, nom="Apple Inc. (AAPL)", type="Action"
        )
        instrument2 = ReferentielInstruments(
            id=2, nom="Microsoft Corporation (MSFT)", type="Action"
        )
        instrument3 = ReferentielInstruments(
            id=3,
            nom="Obligations du Trésor américain (Treasury Bonds)",
            type="Obligation",
        )
        db.session.add_all([instrument1, instrument2, instrument3])

        # Exemples de données pour Positions
        positions = [
        Positions(id=1, fond_id=1, instrument_id=1, prix_actuel=60.00),
        Positions(id=2, fond_id=1, instrument_id=2, prix_actuel=80.00),
        Positions(id=3, fond_id=1, instrument_id=3, prix_actuel=120.00),
        Positions(id=4, fond_id=2, instrument_id=1, prix_actuel=65.00),
        Positions(id=5, fond_id=2, instrument_id=2, prix_actuel=85.00),
        Positions(id=6, fond_id=2, instrument_id=3, prix_actuel=95.00),
        Positions(id=7, fond_id=3, instrument_id=1, prix_actuel=70.00),
        Positions(id=8, fond_id=3, instrument_id=2, prix_actuel=90.00),
        Positions(id=9, fond_id=3, instrument_id=3, prix_actuel=110.00),
         ]
        db.session.add_all(positions)

        # Exemples de données pour Transactions
        transactions = [
            # Transactions pour la position 1
            Transactions(
                position_id=1,
                type_transaction="achat",
                quantite=100,
                prix_transaction=50.00,
                date_transaction=datetime(2024, 1, 10),
            ),
            Transactions(
                position_id=1,
                type_transaction="vente",
                quantite=50,
                prix_transaction=55.00,
                date_transaction=datetime(2024, 2, 15),
            ),
            # Transactions pour la position 2
            Transactions(
                position_id=2,
                type_transaction="achat",
                quantite=200,
                prix_transaction=75.00,
                date_transaction=datetime(2024, 3, 20),
            ),
            Transactions(
                position_id=2,
                type_transaction="vente",
                quantite=100,
                prix_transaction=70.00,
                date_transaction=datetime(2024, 4, 25),
            ),
            # Transactions pour la position 3
            Transactions(
                position_id=3,
                type_transaction="achat",
                quantite=300,
                prix_transaction=100.00,
                date_transaction=datetime(2024, 5, 30),
            ),
            Transactions(
                position_id=3,
                type_transaction="vente",
                quantite=150,
                prix_transaction=110.00,
                date_transaction=datetime(2024, 6, 10),
            ),
            # Transactions pour la position 4
            Transactions(
                position_id=4,
                type_transaction="achat",
                quantite=250,
                prix_transaction=65.00,
                date_transaction=datetime(2024, 7, 15),
            ),
            Transactions(
                position_id=4,
                type_transaction="vente",
                quantite=125,
                prix_transaction=70.00,
                date_transaction=datetime(2024, 8, 20),
            ),
            # Transactions pour la position 5
            Transactions(
                position_id=5,
                type_transaction="achat",
                quantite=180,
                prix_transaction=85.00,
                date_transaction=datetime(2024, 9, 25),
            ),
            Transactions(
                position_id=5,
                type_transaction="vente",
                quantite=90,
                prix_transaction=80.00,
                date_transaction=datetime(2024, 10, 30),
            ),
            # Transactions pour la position 6
            Transactions(
                position_id=6,
                type_transaction="achat",
                quantite=400,
                prix_transaction=90.00,
                date_transaction=datetime(2024, 11, 5),
            ),
            Transactions(
                position_id=6,
                type_transaction="vente",
                quantite=200,
                prix_transaction=95.00,
                date_transaction=datetime(2024, 12, 10),
            ),
            # Transactions pour la position 7
            Transactions(
                position_id=7,
                type_transaction="achat",
                quantite=500,
                prix_transaction=80.00,
                date_transaction=datetime(2024, 1, 15),
            ),
            Transactions(
                position_id=7,
                type_transaction="vente",
                quantite=250,
                prix_transaction=85.00,
                date_transaction=datetime(2024, 2, 20),
            ),
            # Transactions pour la position 8
            Transactions(
                position_id=8,
                type_transaction="achat",
                quantite=150,
                prix_transaction=95.00,
                date_transaction=datetime(2024, 3, 25),
            ),
            Transactions(
                position_id=8,
                type_transaction="vente",
                quantite=75,
                prix_transaction=100.00,
                date_transaction=datetime(2024, 4, 30),
            ),
            # Transactions pour la position 9
            Transactions(
                position_id=9,
                type_transaction="achat",
                quantite=220,
                prix_transaction=110.00,
                date_transaction=datetime(2024, 5, 10),
            ),
            Transactions(
                position_id=9,
                type_transaction="vente",
                quantite=110,
                prix_transaction=115.00,
                date_transaction=datetime(2024, 6, 15),
            ),
        ]
        db.session.add_all(transactions)

        db.session.commit()
        print("Données insérées avec succès !")
    except Exception as e:
        db.session.rollback()  # Annuler la transaction en cas d'erreur
        print(f"Erreur lors de l'insertion des données : {e}")
