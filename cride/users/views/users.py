"""Users views"""


# DJango
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Serializers
from cride.users.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer,
    AccountVerificationSerializer)


class UserLoginAPIView(APIView):
    """USer login api view"""

    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)


class UserSignUpAPIView(APIView):
    """User sign up API view."""

    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)


class AccountVerificationAPIView(APIView):
    """Account verification view"""

    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request."""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data={'message': 'Congratulations, now go shared some rides!!!'}
        return Response(data, status=status.HTTP_200_OK)

