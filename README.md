# Systeme d'authentification en Django

## Aperçu du Projet

Ce projet est une application web Django qui inclut l'authentification des utilisateurs et utilise Tailwind CSS pour le style.

## Configuration

1. **Cloner le dépôt :**

```sh
git clone <repository-url>
cd intro-django
```

2. **Installer les dépendances :**

```sh
pip install -r requirements.txt
```

3. **Appliquer les migrations :**

```sh
python manage.py migrate
```

4. **Lancer le serveur de développement :**

```sh
python manage.py runserver
```

## Structure du Répertoire

- **intro-django/**: Contient les paramètres principaux du projet et les URLs.
- **authentication/**: Contient l'application d'authentification avec les modèles, vues, formulaires et templates.
- **authentication/static/**: Contient les fichiers statiques comme le CSS.
- **authentication/templates/**: Contient les templates HTML.
- **manage.py**: Utilitaire en ligne de commande de Django pour les tâches administratives.
- **tailwind.config.js**: Fichier de configuration pour Tailwind CSS.
- **db.sqlite3**: Fichier de base de données SQLite.

## Licence

Ce projet est sous [licence MIT](LICENSE).
