from rest_framework import serializers
from base.models import WorkoutGif, Client, Exercise
import uuid


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


class ExerciseListSerializer(serializers.ModelSerializer):
    """ lists all exercises """
    status = serializers.SerializerMethodField("get_status")
    type = serializers.SerializerMethodField("get_type")

    class Meta:
        model = Exercise
        fields = ("id", "title", "repeat", "duration", "status", "type", "image")

    def get_status(self, obj):
        return obj.get_status_display()

    def get_type(self, obj):
        return obj.get_type_display()


class CreateExerciseSerializer(serializers.ModelSerializer):
    """ serializer for creating new exercise-object from user's input in dashboard-page"""

    class Meta:
        model = Exercise
        fields = ("title", "type", "token")
        read_only_fields = ("token",)

    def create(self, validated_data):
        unique_value = str(uuid.uuid4())
        request = self.context["request"]
        obj = Exercise.objects.create(
            token=unique_value,
            profile=request.user.profile,
            image=f"exercise_images/{validated_data['type']}.png",
            **validated_data
        )
        return obj


class ExerciseUpdateSerializer(serializers.ModelSerializer):
    """ update exercise """
    class Meta:
        model = Exercise
        fields = ("id", "title", "repeat", "token", "duration", "status", "type", "image")

