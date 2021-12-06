from django.db import models
from .Actor import Actor


class Movie(models.Model):
    adventure = 'Adventure'
    comedy = 'Comedy'
    crime = 'Crime and mystery'

    GENRES = (
        (adventure, 'Adventure'),
        (comedy, 'Comedy'),
        (crime, 'Crime and mystery'),
    )
    name = models.CharField(max_length=150, blank=False, null=False)
    year = models.DateField(blank=False, null=False)
    imdb = models.IntegerField(default=1, blank=False, null=False)
    genrer = models.CharField(max_length=180, choices=GENRES)
    actors = models.ManyToManyField(Actor, related_name='movie')
