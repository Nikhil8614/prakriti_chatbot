from django.db import models

class AyurvedicBodyTest(models.Model):
    user_name = models.CharField(max_length=100)
    q1 = models.CharField(max_length=1, choices=[('A', 'a'), ('B', 'b'), ('C', 'c')])
    # Add fields for other questions
