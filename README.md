# Nom du Projet

Test technique d'une application web de suivi de portefeuilles pour Amiral Gestion.

## Table des matières

- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)

## Installation

### Prérequis

- [MySQL](https://dev.mysql.com/downloads/mysql/)
- [Python](https://www.python.org/downloads/)


1. Clonez le dépôt :
    ```bash
    git clone https://github.com/yourusername/your-repository.git
    cd your-repository/backend
    ```

2. Créez un environnement virtuel et activez-le :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows : venv\Scripts\activate
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4. Copiez le fichier `.env.example` en `.env` :

    ```bash
    cp .env.example .env
    ```
5. Ouvrez le fichier `.env` et définissez les valeurs pour `SQLALCHEMY_DATABASE_URI` :

    ```plaintext
    SQLALCHEMY_DATABASE_URI=your_database_uri_here
    ```

- `SQLALCHEMY_DATABASE_URI` : URI de connexion à la base de données (ex. `mysql://username:password@localhost/dbname`).

6. Initialisez la base de données :
    ```bash
    flask run
    ```

## Configuration

1. **Configuration de la base de données** : Assurez-vous que MySQL est installé et en cours d'exécution. Créez une base de données correspondant à l'URI définie dans `.env`.

2. **Fichier `.env`** : 
    - `SQLALCHEMY_DATABASE_URI` : Spécifiez l'URI de connexion à votre base de données MySQL. Exemple : `mysql://username:password@localhost/portfolio_db`.

## Utilisation

1. **Accéder à l'application** : Une fois le serveur lancé, ouvrez un navigateur web et accédez à `http://127.0.0.1:5000` pour utiliser l'application.

2. **Endpoints disponibles** :

    - **Page d'accueil** :
        - **URL** : `/`
        - **Description** : Affiche un message de bienvenue.
        - **Template utilisé** : `index.html`

    - **Voir les fonds** :
        - **URL** : `/fonds`
        - **Description** : Affiche la liste des fonds disponibles.
        - **Template utilisé** : `fonds.html`
        - **Variables** : `fonds` - Liste des fonds.

    - **Voir les instruments financiers** :
        - **URL** : `/instruments`
        - **Description** : Affiche la liste des instruments financiers disponibles.
        - **Template utilisé** : `instruments.html`
        - **Variables** : `instruments` - Liste des instruments.

    - **Voir les positions pour un fonds** :
        - **URL** : `/positions/<int:fond_id>`
        - **Description** : Affiche les positions d'un fonds spécifique.
        - **Template utilisé** : `positions.html`
        - **Paramètre** : `fond_id` - ID du fonds.
        - **Variables** : `positions` - Liste des positions pour le fonds spécifié.

    - **Voir l'historique des transactions pour une position** :
        - **URL** : `/positions/<int:position_id>/historique`
        - **Description** : Affiche l'historique des transactions pour une position donnée.
        - **Template utilisé** : `transaction_historique.html`
        - **Paramètre** : `position_id` - ID de la position.
        - **Variables** : 
            - `position` - Données de la position.
            - `transactions` - Liste des transactions associées à la position.

