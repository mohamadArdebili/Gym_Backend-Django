from django.contrib import admin
from base.models import Profile, User, WorkoutGif, Exercise, Client

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(WorkoutGif)
admin.site.register(Exercise)
admin.site.register(Client)
