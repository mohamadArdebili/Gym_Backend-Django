from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from base.general.serializers import WorkoutGifListSerializer, ClientsListSerializer
from base.models import WorkoutGif, Client


class WorkoutGifListView(ListAPIView):
    """ listing all the workout gifs """
    queryset = WorkoutGif.objects.all()
    serializer_class = WorkoutGifListSerializer


class ClientGifListView(ListAPIView):
    """ listing all objs of what clients have said in homepage """
    queryset = Client.objects.all()
    serializer_class = ClientsListSerializer
