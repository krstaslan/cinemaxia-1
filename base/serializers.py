from rest_framework import serializers
from .models import Movie,Rezervation

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class RezervationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezervation
        fields = '__all__'