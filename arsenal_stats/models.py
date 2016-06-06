from django.db import models


class Player(models.Model):
    full_name = models.CharField(max_length=30)
    position = models.CharField(max_length=3)
    age = models.IntegerField()
    number = models.IntegerField()
    games_started = models.IntegerField()
    goals_scored = models.IntegerField()
    assists = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()

    def __str__(self):
        return self.full_name
