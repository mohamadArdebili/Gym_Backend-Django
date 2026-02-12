from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from base.general.serializers import (
    WorkoutGifListSerializer, ClientsListSerializer,
    ExerciseListSerializer, CreateExerciseSerializer,
    ExerciseUpdateSerializer,
)
from base.models import WorkoutGif, Client, Exercise


class WorkoutGifListView(ListAPIView):
    """ listing all the workout gifs """
    queryset = WorkoutGif.objects.all()
    serializer_class = WorkoutGifListSerializer


class ClientGifListView(ListAPIView):
    """ listing all objs of what clients have said in homepage """
    queryset = Client.objects.all()
    serializer_class = ClientsListSerializer


class ExerciseCreateListView(ListCreateAPIView):
    """ list and create exercise-objects """
    def get_queryset(self):
        """ return exercise for each user """
        return Exercise.objects.filter(
            profile=self.request.user.profile
        )

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateExerciseSerializer
        elif self.request.method == "GET":
            return ExerciseListSerializer


class ExerciseUpdateView(RetrieveUpdateAPIView):
    """ return & update a single exercise object """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseUpdateSerializer
    lookup_field = "token"

