from rest_framework import serializers
from base.models import WorkoutGif, Client


class WorkoutGifListSerializer(serializers.ModelSerializer):
    """ serializer for WorkoutGif model """

    class Meta:
        model = WorkoutGif
        fields = ("id", "gif")


class ClientsListSerializer(serializers.ModelSerializer):
    """ lists what clients say (clients' opinion in homepage) """
    class Meta:
        model = Client
        fields = ("id", "name", "opinion", "image")
