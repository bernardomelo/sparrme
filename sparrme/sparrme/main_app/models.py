from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models


class FightingStyle(models.TextChoices):
    kMuayThai = "MUAYTHAI", "MuayThai"
    kBoxe = "BOXE", "Boxe"
    kKarate = "KARATE", "Karate"
    kJudo = "JUDO", "Judo"
    kBJJ = "BJJ", "BJJ"
    kMMA = "MMA", "MMA"


class Fighter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default=None, null=True, blank=True)
    birth_date = models.DateField(default=None, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    main_style = models.CharField(choices=FightingStyle.choices, default=None)
    location = models.PointField()


class FighterCard(models.Model):
    fighter = models.ForeignKey(Fighter, on_delete=models.CASCADE)
    style = models.CharField(choices=FightingStyle.choices, default=None)
    wins = models.IntegerField(default=None, null=True, blank=True)
    draws = models.IntegerField(default=None, null=True, blank=True)
    loses = models.IntegerField(default=None, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)


class Fights(models.Model):
    title = models.CharField(max_length=255, default=None, null=True, blank=True)
    style = models.CharField(choices=FightingStyle.choices, default=None)
    fighters = models.ManyToManyField(Fighter)
    location = models.PointField()
    create_date = models.DateTimeField(auto_now_add=True, editable=False)


class FinishedFights(models.Model):
    fight = models.ForeignKey(Fights, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default=None, null=True, blank=True)
    style = models.CharField(choices=FightingStyle.choices, default=None)
    winner = models.ManyToManyField(Fighter) # If there is more than 1 winner = DRAW
    location = models.PointField()
    create_date = models.DateTimeField(auto_now_add=True, editable=False)


class SparringSession(models.Model):
    title = models.CharField(max_length=255, default=None, null=True, blank=True)
    style = models.CharField(choices=FightingStyle.choices, default=None)
    fighters = models.ManyToManyField(Fighter)
    location = models.PointField()
    create_date = models.DateTimeField(auto_now_add=True, editable=False)


class FinishedSparring(models.Model):
    session = models.ForeignKey(SparringSession, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default=None, null=True, blank=True)
    style = models.CharField(choices=FightingStyle.choices, default=None)
    location = models.PointField()
    create_date = models.DateTimeField(auto_now_add=True, editable=False)