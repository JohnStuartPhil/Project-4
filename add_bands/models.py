from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

STATUS = ((0, "Draft"), (1, "Published"))
GENRE_CHOICES = (('Please select', 'PLEASE SELECT'), ('Pop', 'POP'),('Rock', 'ROCK'),('Blues', 'BLUES'),('Jazz', 'JAZZ'),('Other', 'OTHER'),)
VENUE_CHOICES = (('Please select', 'PLEASE SELECT'), ('Pub', 'PUB'), ('Club', 'CLUB'), ('Arena', 'ARENA'), ('Stadium', 'STADIUM'))
#NUMBER_OF_MEMEBRS_CHOICES = (('Please select', 'PLEASE SELECT'), ('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6 or more', '6 OR MORE'),)
#MARKS_OUT_OF_FIVE_CHOICES = (('Please select', 'PLEASE SELECT'), ('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),)

# Create your models here.


class BandPost(models.Model):
    name_of_band = models.CharField(max_length=25, unique=False)
    genre = models.CharField(choices=GENRE_CHOICES, default='Please select', unique=False)
    size_of_venue_played = models.CharField(choices=VENUE_CHOICES, default='Please select', unique=False)
    number_of_members = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(99)], unique=False)
    marks_out_of_five = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], unique=False)
    # number_of_members = models.CharField(choices=NUMBER_OF_MEMEBRS_CHOICES, default='Please select', unique=False)
    # marks_out_of_five = models.CharField(choices=MARKS_OUT_OF_FIVE_CHOICES, default='Please select', unique=False)
    band_review = models.TextField(unique=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="band_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    # approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.name_of_band} | written by {self.author}"












#class Opinion(models.Model):
    #name_of_band = models.ForeignKey(BandPost, on_delete=models.CASCADE, related_name="opinions")
    #marks_out_of_five = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], unique=False)
    #your_thoughts = models.TextField(unique=False)
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="opinionator")
    #created_on = models.DateTimeField(auto_now_add=True)
    #updated_on = models.DateTimeField(auto_now=True)
    #approved = models.BooleanField(default=False)

    #class Meta:
     #   ordering = ["created_on"]

    #def __str__(self):
     #   return f"Opinion {self.your_thoughts} by {self.author}"
