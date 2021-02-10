from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import RegisterView, LoginView

urlpatterns = [
    path("register/", view=RegisterView.as_view(), name="register"),
    path("login/", view=LoginView.as_view(), name="login"),
    # SimpleJWT URLs
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
