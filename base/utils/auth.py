from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken


def generate_token_for_user(user):
    """ generate access & refresh token & has_profile for user """
    tokens = RefreshToken.for_user(user)
    update_last_login(sender=None, user=user)
    response = {
        "refresh": str(tokens),
        "access": str(tokens.access_token),
        "has_profile": hasattr(user, "profile")
    }
    return response
