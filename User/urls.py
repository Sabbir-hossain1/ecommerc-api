from django.urls import path, include
from rest_framework.routers import DefaultRouter
from User.views.users_view import UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

userRouter = DefaultRouter()
userRouter.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(userRouter.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
