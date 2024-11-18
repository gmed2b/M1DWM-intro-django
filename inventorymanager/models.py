from django.db import models

# Create your models here.
class Player(models.Model):
  player_name = models.CharField(max_length=100)
  player_level = models.IntegerField(default=0)

  def __str__(self):
      return f"{self.player_name} (Level {self.player_level})"


class Inventory(models.Model):
  player = models.ForeignKey(Player, on_delete=models.CASCADE)
  item_name = models.CharField(max_length=100)
  item_type = models.CharField(max_length=100)
  item_quantity = models.IntegerField()

  def __str__(self):
      return f"{self.item_name} ({self.item_type}, {self.item_quantity})"
