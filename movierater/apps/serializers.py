from rest_framework import serializers
from .models import Movie, Rating


class Movieserializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "description")


class Ratingserializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("id", "movie", "user", "stars")
