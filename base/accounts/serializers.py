from rest_framework import serializers
from rest_framework import status
from base.models import User, Profile
from base.utils.exceptions import CustomException
from base.utils.caching import CachingProcedureHandler
from base.utils.constants import Constant
from base.utils.emails import EmailHandler


class UserCreationSerializer(serializers.ModelSerializer):
    """ create user serializer """

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ProfileCreationSerializer(serializers.ModelSerializer):
    """ create user's-profile serializer """
    BMI = serializers.FloatField(read_only=True)
    user = UserCreationSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ("age", "weight", "height", "avatar", "description", "user", "BMI")

    def validate(self, attrs):
        request = self.context["request"]
        user = request.user

        # check if the user has already created a profile
        profiles = Profile.objects.filter(user=user)
        if profiles.exists():
            raise CustomException(
                field="error",
                detail="You have already created a profile",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        return super().validate(attrs)

    def create(self, validated_data):
        user = self.context["request"].user
        weight = validated_data["weight"]
        height = validated_data["height"]
        BMI = round(weight / (height / 100) ** 2, 1)
        profile = Profile.objects.create(
            user=user,
            BMI=BMI,
            **validated_data
        )
        return profile


class LoginRequestSerializer(serializers.Serializer):
    """ user sends email to request for login  """
    email = serializers.EmailField()

    def validate(self, attrs):
        """ checking if the email already exists """
        try:
            User.objects.get(email=attrs["email"])
        except User.DoesNotExist:
            raise CustomException(
                field="error",
                detail="User with this email does not exist!",
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        return super().validate(attrs)

    def send_token(self):
        """ generate token, store in cache and send using email """
        caching_handler = CachingProcedureHandler()
        email_handler = EmailHandler()
        email = self.data["email"]
        token = caching_handler.generate_token()
        result = caching_handler.set_key(
            type=Constant.LOGIN_TYPE_CACHING,
            email=email,
            token=token
        )
        if not result:
            raise CustomException(
                field="error",
                detail="failed to store token!",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        # sending otp email
        email_handler.send_otp(email=email, token=token)


class VerifyTokenSerializer(serializers.Serializer):
    """ get user's token(otp) and validate it """
    token = serializers.CharField()

    def validate(self, attrs):
        """ validate user token """
        caching_handler = CachingProcedureHandler()
        token = attrs["token"]
        # checking for key in cache
        email = caching_handler.get_key(type=Constant.LOGIN_TYPE_CACHING, token=token)
        if email is None:
            raise CustomException(
                field="error",
                detail="token is not valid!",
                status_code=status.HTTP_403_FORBIDDEN
            )
        # updating validated_data with 'email' key
        attrs.update({
            "email": email
        })
        return attrs

    def get_user(self):
        email = self.validated_data["email"]
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise CustomException(
                field="error",
                detail="requested user does not exist!",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        return user
