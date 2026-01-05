from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from base.general.serializers import WorkoutGifSerializer
from base.models import WorkoutGif


class WorkoutGifListView(ListAPIView):
    """ listing all the workout gifs """
    queryset = WorkoutGif.objects.all()
    serializer_class = WorkoutGifSerializer


