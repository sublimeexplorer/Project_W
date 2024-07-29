from django.db import models
from main_server.members.models import CustomUser

class MealPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    trainer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_meal_plans')
    clients = models.ManyToManyField(CustomUser, related_name='assigned_meal_plans')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Meal(models.Model):
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    calories = models.IntegerField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fats = models.FloatField()