from django.db import models


class Actor(models.Model):
    GEN = (
        ("MALE", 'MALE'),
        ("FEMALE", 'FEMALE'),
    )

    name = models.CharField(max_length=120)
    birthdate = models.DateField()
    gender = models.CharField(max_length=20, choices=GEN)
