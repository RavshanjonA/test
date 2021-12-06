from rest_framework import serializers
from .models.Actor import Actor
from .models.Movie import Movie
from rest_framework.exceptions import ValidationError

class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'birthdate', 'gender')

    def validate_source(self, value):
        if not value.startwith('01.01.1950'):
            return ValidationError(detail='01.01.1950 boshlansin')

        return value


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'year', 'imdb', 'genre', 'actors')
