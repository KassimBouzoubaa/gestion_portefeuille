from . import db
from datetime import datetime


class ReferentielFonds(db.Model):
    """
    Représente un fonds d'investissement.

    Attributs:
        id (int): Identifiant unique du fonds.
        nom (str): Nom du fonds (ex. "Fonds A").
    """

    __tablename__ = "referentiel_fonds"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)


class ReferentielInstruments(db.Model):
    """
    Représente un instrument financier.

    Attributs:
        id (int): Identifiant unique de l'instrument.
        nom (str): Nom de l'instrument (ex. "Action XYZ").
        type (str): Type de l'instrument (ex. "Action", "Obligation").
    """

    __tablename__ = "referentiel_instruments"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)


class Transactions(db.Model):
    """
    Représente une transaction effectuée sur une position d'investissement.
    """

    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    position_id = db.Column(db.Integer, db.ForeignKey("positions.id"), nullable=False)
    date_transaction = db.Column(db.DateTime, nullable=False, default=datetime.now)
    type_transaction = db.Column(db.String(10), nullable=False)  # 'achat' ou 'vente'
    quantite = db.Column(db.Numeric(10, 2), nullable=False)
    prix_transaction = db.Column(db.Numeric(10, 2), nullable=False)

    position = db.relationship('Positions', back_populates='transactions')

    def __init__(
        self,
        position_id,
        type_transaction,
        quantite,
        prix_transaction,
        date_transaction=None,
    ):
        self.position_id = position_id
        self.type_transaction = type_transaction
        self.quantite = quantite
        self.prix_transaction = prix_transaction
        if date_transaction:
            self.date_transaction = date_transaction

    @property
    def valeur_transaction(self):
        """Calcul de la valeur totale de la transaction (quantité * prix)."""
        return round(float(self.quantite) * float(self.prix_transaction), 2)

    def __repr__(self):
        return f"<Transaction {self.type_transaction} de {self.quantite} unités à {self.prix_transaction} € le {self.date_transaction}>"


class Positions(db.Model):
    """
    Représente une position d'investissement dans un fonds pour un instrument financier donné.
    """

    __tablename__ = "positions"

    id = db.Column(db.Integer, primary_key=True)
    fond_id = db.Column(
        db.Integer, db.ForeignKey("referentiel_fonds.id"), nullable=False
    )
    instrument_id = db.Column(
        db.Integer, db.ForeignKey("referentiel_instruments.id"), nullable=False
    )

    prix_actuel = db.Column(db.Float, nullable=False, default=0.0)
    fond = db.relationship(
        "ReferentielFonds", backref=db.backref("positions", lazy=True)
    )
    instrument = db.relationship(
        "ReferentielInstruments", backref=db.backref("positions", lazy=True)
    )
    transactions = db.relationship('Transactions', back_populates='position')

    @property
    def quantite(self):
        """Calcule la quantité totale de l'instrument détenue en fonction des transactions associées."""
        return sum(t.quantite for t in self.transactions)

    @property
    def prix_achat_moyen(self):
        """Calcule le prix d'achat moyen basé sur les transactions associées."""
        total_quantite = sum(t.quantite for t in self.transactions)
        total_cost = sum(t.quantite * t.prix_transaction for t in self.transactions)
        return round(total_cost / total_quantite, 2) if total_quantite > 0 else 0.0

    @property
    def gain_perte_valeur(self):
        """Calcul du gain/perte en valeur absolue avec arrondi à deux décimales et ajout d'un signe '+' si le résultat est positif."""
        if self.quantite > 0:
            valeur = float(self.quantite) * (
                float(self.prix_actuel) - float(self.prix_achat_moyen)
            )
            return f"+{round(valeur, 2)}" if valeur > 0 else f"{round(valeur, 2)}"
        return "0.00"

    @property
    def gain_perte_ratio(self):
        """Calcul du gain/perte en pourcentage."""
        if self.prix_achat_moyen > 0 and self.quantite > 0:
            pourcentage = (
                (float(self.prix_actuel) - float(self.prix_achat_moyen))
                / float(self.prix_achat_moyen)
            ) * 100
            return (
                f"+{round(pourcentage, 2)}%"
                if pourcentage > 0
                else f"{round(pourcentage, 2)}%"
            )
        return "0.00%"
