from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as octofit_models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **options):
        # Use PyMongo to clear collections
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db['octofit_tracker_user'].delete_many({})
        db['octofit_tracker_team'].delete_many({})
        db['octofit_tracker_activity'].delete_many({})
        db['octofit_tracker_leaderboard'].delete_many({})
        db['octofit_tracker_workout'].delete_many({})

        # Create teams
        marvel = octofit_models.Team.objects.create(name='Marvel')
        dc = octofit_models.Team.objects.create(name='DC')

        # Create users
        ironman = get_user_model().objects.create_user(username='ironman', email='ironman@marvel.com', team=marvel)
        captain = get_user_model().objects.create_user(username='captainamerica', email='cap@marvel.com', team=marvel)
        batman = get_user_model().objects.create_user(username='batman', email='batman@dc.com', team=dc)
        superman = get_user_model().objects.create_user(username='superman', email='superman@dc.com', team=dc)

        # Create activities
        octofit_models.Activity.objects.create(user=ironman, type='run', distance=5)
        octofit_models.Activity.objects.create(user=batman, type='cycle', distance=20)

        # Create workouts
        octofit_models.Workout.objects.create(user=captain, description='Pushups', reps=50)
        octofit_models.Workout.objects.create(user=superman, description='Squats', reps=100)

        # Create leaderboard
        octofit_models.Leaderboard.objects.create(team=marvel, points=100)
        octofit_models.Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
