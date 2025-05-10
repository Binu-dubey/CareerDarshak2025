from django.db import models
from django.contrib.auth.models import User  # Import Django's User model
from django.contrib.postgres.fields import JSONField  # or use models.JSONField in Django 3.1+
# --- Level 1 Assessment Models ---

class Question(models.Model):
    level = models.IntegerField()
    question_number = models.IntegerField()
    question_text = models.TextField()
    trait = models.CharField(max_length=100)

    def __str__(self):
        return f"Q{self.question_number}: {self.question_text[:50]}"


class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.text} ({self.score})"


# --- User Responses (Link user to selected options) ---

class UserResponse(models.Model):
    user = models.ForeignKey(User, related_name='responses', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} answered Q{self.question.question_number}"


# --- Trait Score (used as ML model input) ---

class TraitScore(models.Model):
    user = models.ForeignKey(User, related_name='trait_scores', on_delete=models.CASCADE)
    trait = models.CharField(max_length=100)
    score = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.trait}: {self.score}"


# --- ML Prediction Output ---


class MLPredictionResult(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    predicted_personality = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    key_strengths = models.JSONField(default=list)
    growth_areas = models.JSONField(default=list)
    radar_scores = models.JSONField(default=dict)  # e.g., {"Self-Learning": 80, "Communication": 60}

