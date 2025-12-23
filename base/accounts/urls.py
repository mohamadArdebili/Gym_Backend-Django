from django.urls import path
from base.accounts.views import UserCreationView

# 127.0.0.1:8000/api/accounts/...

urlpatterns = [
    path("signup/", UserCreationView.as_view(), name="create_user"),
]
