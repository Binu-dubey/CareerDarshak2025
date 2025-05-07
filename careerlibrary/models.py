from django.db import models

# Create your models here.
class CareerOption(models.Model):
    STREAM_CHOICES = [
        ('Science', 'Science'),
        ('Commerce', 'Commerce'),
        ('Arts', 'Arts'),
        ('Any','Any')
    ]
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='career_images/')
    description = models.TextField()
    stream_type = models.CharField(
    max_length=50,
    choices=STREAM_CHOICES,
    default='Science'  # or any default you'd like
)

    def __str__(self):
        return self.name

class Branch(models.Model):
    career_option = models.ForeignKey(CareerOption, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='branch_images/')
    description = models.TextField()
    video = models.FileField(upload_to='branch_videos/')  # Uploading videos locally
    career_path_image = models.ImageField(upload_to='career_path_images/')
    opportunities = models.TextField()  # Career opportunities for the branch
    average_salary = models.CharField(max_length=100)
    pros = models.TextField()
    cons = models.TextField()

    def __str__(self):
        return self.name