from rest_framework.views import APIView
from rest_framework.response import Response

from .models.Movie import Movie
from .models.Actor import Actor
from .serializer import ActorSerializers, MovieSerializers


class MovieAPIView(APIView):
    def get(self, request):
        movie = Movie.objects.all()
        serializers = MovieSerializers(movie, many=True)
        return Response(data=serializers.data)


class ActorAPIView(APIView):
    def get(self, request):
        actor = Actor.objects.all()
        serializers = ActorSerializers(actor, many=True)
        return Response(data=serializers.data)
