from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)
from base.accounts.views import (
    UserCreationView, ProfileCreationView,
    LoginRequestView, VerifyTokenView
)

# 127.0.0.1:8000/api/accounts/...

urlpatterns = [
    path("signup/", UserCreationView.as_view(), name="create_user"),
    path("profile/create/", ProfileCreationView.as_view(), name="create_profile"),
    path("signin/", LoginRequestView.as_view(), name="login_request"),
    path("verify-token/", VerifyTokenView.as_view(), name="verify_otp"),

    # JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
