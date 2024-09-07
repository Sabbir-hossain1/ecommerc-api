from rest_framework import exceptions
from rest_framework_simplejwt.authentication import JWTAuthentication
import jwt
from django.http import JsonResponse
from rest_framework import status


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        try:
            return super().authenticate(request)
        except exceptions.AuthenticationFailed as e:
            print("Authentication failed:", str(e))
            if isinstance(e.__cause__, jwt.exceptions.InvalidTokenError):
                return JsonResponse(
                    {"error": "Invalid token"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            return JsonResponse({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
