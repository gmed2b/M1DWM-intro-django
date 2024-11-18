import random
from faker import Faker
from django.core.management.base import BaseCommand
from inventorymanager.models import Player, Inventory

# Initialiser Faker
fake = Faker()

class Command(BaseCommand):  # La classe doit s'appeler Command et hériter de BaseCommand
    help = "Populate the database with fake Player and Inventory data"  # Description de la commande

    def handle(self, *args, **kwargs):
        self.populate_database()

    def populate_database(self):
        """Crée des joueurs et leurs objets factices dans la base de données."""
        # Créer un joueur factice
        player_name = fake.name()
        player_level = random.randint(1, 50)
        player = Player.objects.create(
            player_name = player_name,
            player_level= player_level,
        )
        self.stdout.write(self.style.SUCCESS(f"Created player: {player.player_name} (Level: {player.player_level})"))

        # Types d'items possibles
        item_types = ["Weapon", "Armor", "Potion", "Scroll", "Gem"]

        # Créer 10 items pour ce joueur
        for _ in range(10):
            item_name = fake.word().capitalize()
            item_quantity = random.randint(1, 20)
            item_type = random.choice(item_types)

            item = Inventory.objects.create(
                item_name=item_name,
                item_quantity=item_quantity,
                item_type=item_type,
                player=player,
            )
            self.stdout.write(f"Created item: {item.item_name} (Type: {item.item_type}, Quantity: {item.item_quantity})")

        self.stdout.write(self.style.SUCCESS("Database populated successfully!"))
