from rest_framework import serializers
from base.models import User, Profile


class UserCreationSerializer(serializers.ModelSerializer):
    """ create user serializer """
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

