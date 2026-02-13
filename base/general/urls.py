from django.urls import path
from base.general.views import (
    WorkoutGifListView, ClientGifListView,
    ExerciseCreateListView, ExerciseUpdateView
)


# 127.0.0.1:8000/api/general/...
urlpatterns = [
    path("workouts/", WorkoutGifListView.as_view(), name="list_all_workouts"),
    path("clients/", ClientGifListView.as_view(), name="list_all_clients"),
    path("exercise/", ExerciseCreateListView.as_view(), name="list_and_create_exercise"),
    path("exercise/<str:token>/", ExerciseUpdateView.as_view(), name="list_and_create_exercise"),
]
