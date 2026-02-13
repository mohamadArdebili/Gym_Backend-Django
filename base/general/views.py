from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from base.general.serializers import (
    WorkoutGifListSerializer, ClientsListSerializer,
    ExerciseListSerializer, CreateExerciseSerializer,
    ExerciseUpdateSerializer,
)
from base.models import WorkoutGif, Client, Exercise
from base.utils.permissions import HasProfile


class WorkoutGifListView(ListAPIView):
    """ listing all the workout gifs object """
    queryset = WorkoutGif.objects.all()
    serializer_class = WorkoutGifListSerializer


class ClientGifListView(ListAPIView):
    """ listing all objs of what clients have said in homepage """
    queryset = Client.objects.all()
    serializer_class = ClientsListSerializer


class ExerciseCreateListView(ListCreateAPIView):
    """ list and create exercise-objects """
    permission_classes = (HasProfile, )

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
    permission_classes = (HasProfile, )

    queryset = Exercise.objects.all()
    serializer_class = ExerciseUpdateSerializer
    lookup_field = "token"

