from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    id = models.ObjectIdField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True, db_column='team_id')

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id')
    type = models.CharField(max_length=50)
    distance = models.FloatField()

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id')
    description = models.CharField(max_length=100)
    reps = models.IntegerField()

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, db_column='team_id')
    points = models.IntegerField()
