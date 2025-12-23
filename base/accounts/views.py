from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from base.accounts.serializers import (
    UserCreationSerializer, ProfileCreationSerializer
)
from base.models import User, Profile
from base.utils.auth import generate_token_for_user


# @api_view(["POST"])
# def create_user(request):
#     """ create a new user """
#     if request.method == "POST":
#         serialized = UserCreationSerializer(data=request.data)
#         serialized.is_valid(raise_exception=True)
#         serialized.save()
#         return Response(data=serialized.data, status=status.HTTP_201_CREATED)

class UserCreationView(GenericAPIView):
    """ create a new user """
    serializer_class = UserCreationSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serialized = self.get_serializer(data=request.data, context={"request": request})
        serialized.is_valid(raise_exception=True)
        user = serialized.save()
        response = generate_token_for_user(user)
        return Response(data=response, status=status.HTTP_201_CREATED)


class ProfileCreationView(CreateAPIView):
    """ create a new profile """
    queryset = Profile
    serializer_class = ProfileCreationSerializer
