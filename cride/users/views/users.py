"""Users views"""


# DJango
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Serializers
from cride.users.serializers import (UserLoginSerializer, UserModelSerializer, UserSignUpSerializer)


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
    """User signup api view"""

    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(request.data).data,
        return Response(data, status=status.HTTP_201_CREATED)
