from rest_framework import serializers
from base.models import WorkoutGif


class WorkoutGifSerializer(serializers.ModelSerializer):
    """ serializer for WorkoutGif model """
    class Meta:
        model = WorkoutGif
        fields = ("id", "gif")



class
