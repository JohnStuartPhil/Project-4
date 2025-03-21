from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

STATUS = ((0, "Draft"), (1, "Published"))
GENRE_CHOICES = (('genre', 'GENRE'), ('pop', 'POP'),('rock', 'ROCK'),('blues', 'BLUES'),('jazz', 'JAZZ'),('other', 'OTHER'),)

# Create your models here.
class Post(models.Model):
    name_of_band = models.CharField(max_length=25, unique=True)
    genre = models.CharField(max_length=6, choices=GENRE_CHOICES, default='genre')
    number_of_members = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)], unique=False)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], unique=False)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="band_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)