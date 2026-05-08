from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Daten löschen
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel')
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='dc')
        wonderwoman = User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='dc')
        spiderman = User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='marvel')

        # Activities
        Activity.objects.create(user='Iron Man', activity_type='run', duration=30, date='2024-01-01')
        Activity.objects.create(user='Batman', activity_type='cycle', duration=45, date='2024-01-02')
        Activity.objects.create(user='Wonder Woman', activity_type='swim', duration=60, date='2024-01-03')
        Activity.objects.create(user='Spider-Man', activity_type='jump', duration=20, date='2024-01-04')

        # Leaderboard
        Leaderboard.objects.create(user='Iron Man', points=100)
        Leaderboard.objects.create(user='Batman', points=120)
        Leaderboard.objects.create(user='Wonder Woman', points=110)
        Leaderboard.objects.create(user='Spider-Man', points=90)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Situps', description='Do 30 situps', difficulty='medium')
        Workout.objects.create(name='Squats', description='Do 40 squats', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db erfolgreich mit Testdaten befüllt.'))
