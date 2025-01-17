from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    CATEGORY_CHOICES = [
        ('psychometric', 'Psychometric'),
        ('aptitude', 'Aptitude'),
        ('reasoning', 'Reasoning'),
    ]
    SUBCATEGORY_CHOICES = [
        ('o_score', 'O Score'),
        ('c_score', 'C Score'),
        ('e_score', 'E Score'),
        ('a_score', 'A Score'),
        ('n_score', 'N Score'),
        ('numerical','Numerical'),
        ('verbal', 'Verbal'),
        ('logical', 'Logical'),
    ]
    
    question_text = models.TextField()
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    subcategory = models.CharField(max_length=255, choices=SUBCATEGORY_CHOICES)
    
    # Options and the correct answer
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    
    correct_option = models.CharField(max_length=255)
    
    # Scores for each option (e.g., 1-5 scale)
    option_1_score = models.IntegerField(default=0)
    option_2_score = models.IntegerField(default=0)
    option_3_score = models.IntegerField(default=0)
    option_4_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.question_text} ({self.subcategory})"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Psychometric scores
    o_score = models.FloatField(default=0)
    c_score = models.FloatField(default=0)
    e_score = models.FloatField(default=0)
    a_score = models.FloatField(default=0)
    n_score = models.FloatField(default=0)
    # Aptitude scores
    numerical_ability = models.FloatField(default=0)
   
    # Reasoning scores
    verbal_reasoning = models.FloatField(default=0)
    logical_reasoning = models.FloatField(default=0)
