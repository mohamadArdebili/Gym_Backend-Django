from rest_framework import serializers
from base.models import User, Profile


class UserCreationSerializer(serializers.ModelSerializer):
    """ create user serializer """

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ProfileCreationSerializer(serializers.ModelSerializer):
    """ create user's-profile serializer """

    class Meta:
        model = Profile
        fields = ("age", "weight", "height", "avatar", "description")
