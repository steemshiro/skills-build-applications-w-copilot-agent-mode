from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Marvel", description="Marvel superheroes")
        self.user = User.objects.create(name="Tony Stark", email="tony@stark.com", team=self.team, is_superhero=True)

    def test_user_email_unique(self):
        with self.assertRaises(Exception):
            User.objects.create(name="Duplicate", email="tony@stark.com", team=self.team)

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="DC", description="DC superheroes")
        self.assertEqual(team.name, "DC")

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        team = Team.objects.create(name="Marvel")
        user = User.objects.create(name="Bruce Banner", email="bruce@hulk.com", team=team)
        activity = Activity.objects.create(user=user, type="Running", duration=30, date="2025-12-15")
        self.assertEqual(activity.type, "Running")

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Pushups", description="Upper body strength")
        self.assertEqual(workout.name, "Pushups")

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        team = Team.objects.create(name="Marvel")
        leaderboard = Leaderboard.objects.create(team=team, score=100)
        self.assertEqual(leaderboard.score, 100)
