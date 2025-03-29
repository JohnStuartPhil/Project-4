from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

STATUS = ((0, "Draft"), (1, "Published"))
GENRE_CHOICES = (('genre', 'GENRE'), ('pop', 'POP'),('rock', 'ROCK'),('blues', 'BLUES'),('jazz', 'JAZZ'),('other', 'OTHER'),)

# Create your models here.
class Band_Post(models.Model):
    name_of_band = models.CharField(max_length=25, unique=False)
    genre = models.CharField(max_length=6, choices=GENRE_CHOICES, default='genre', unique=False)
    number_of_members = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)], unique=False)
    marks_out_of_five = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], unique=False)
    band_review = models.TextField(unique=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="band_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.name_of_band} | written by {self.author}"

class Opinion(models.Model):
    name_of_band = models.ForeignKey(Band_Post, on_delete=models.CASCADE, related_name="opinions")
    marks_out_of_five = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], unique=False)
    your_thoughts = models.TextField(unique=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="opinionator")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Opinion {self.your_thoughts} by {self.author}"
