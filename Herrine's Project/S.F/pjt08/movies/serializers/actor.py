from rest_framework import serializers
from ..models import Actor, Movie

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title',)

class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('id', 'movies', 'name')


