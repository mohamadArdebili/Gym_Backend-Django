from django.urls import path, include

# 127.0.0.1:8000/api/...

urlpatterns = [
    path("accounts/", include("base.accounts.urls")),
    path("general/", include("base.general.urls")),
]
