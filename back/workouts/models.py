from django.db import models
from main_server.members.models import CustomUser

class WorkoutPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    trainer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_workouts')
    clients = models.ManyToManyField(CustomUser, related_name='assigned_workouts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField(blank=True)

class WorkoutSession(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    rest_time = models.IntegerField()  # in seconds