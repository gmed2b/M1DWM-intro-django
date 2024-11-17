import os
import django
from faker import Faker

# Initialiser Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'votre_projet.settings')
django.setup()

# Importer vos modèles
from votre_app.models import Utilisateur, Maquette_formation, Cycle  # Ajoutez les autres modèles nécessaires

# Initialiser Faker
fake = Faker()

# Fonction pour créer un utilisateur factice
def create_fake_user():
    return Utilisateur.objects.create(
        email=fake.email(),
        password=fake.password(),
        # Ajoutez d'autres champs selon vos modèles
    )

# Fonction pour créer une maquette de formation factice
def create_fake_maquette_formation():
    return Maquette_formation.objects.create(
        nom=fake.word(),
        description=fake.sentence(),
        # Ajoutez d'autres champs nécessaires
    )

# Fonction pour créer un cycle de formation factice
def create_fake_cycle():
    return Cycle.objects.create(
        nom=fake.word(),
        description=fake.sentence(),
        # Ajoutez d'autres champs nécessaires
    )

# Créer des données factices
def populate_db():
    # Créer 10 utilisateurs factices
    for _ in range(10):
        create_fake_user()
    
    # Créer 5 maquettes de formation factices
    for _ in range(5):
        create_fake_maquette_formation()
    
    # Créer 3 cycles de formation factices
    for _ in range(3):
        create_fake_cycle()

    print("Base de données remplie avec des données factices!")

# Lancer le script
if __name__ == '__main__':
    populate_db()
