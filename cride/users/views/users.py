"""Users views."""

# Django REST Framework
from cride.users.serializers.profile import ProfileModelSerializer
from cride.circles import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from cride.users.permissions import IsAccountOwner
from cride.circles.models import Circle
from cride.circles.serializers import CircleModelSerializer
# Model
from cride.users.models import User

# Serializers
from cride.users.serializers import (
    AccountVerificationSerializer,
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer
)


class UserViewSet(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet):
    """User view set
    Handle login account verification
    """
    queryset = User.objects.filter(is_client=True, is_active=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_permission(self):
        if self.action in ['login', 'verify', 'signup']:
            permissions = [AllowAny]
        elif self.actions == ['retrive', 'update']:
            permissions = [IsAuthenticated, IsAccountOwner]

        else:
            permissions = [IsAuthenticated]

        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def login(self, request):
        """Handle HTTP POST request."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """Handle HTTP POST request."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def verify(self, request):
        """Handle HTTP POST request."""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Congratulation, now go share some rides!'}
        return Response(data, status=status.HTTP_200_OK)


    @action(detail=True, methods=['patch', 'put'])
    def profile(self, request, *args, **kwargs):
        user = self.get_object()
        profile = user.profile
        partial = request.method == 'PATCH'
        serializer = ProfileModelSerializer(
            data= request.data,
            partial = partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data
        return Response(data)



    def retrieve(self, request, *args, **kwargs):
        """Add extra data to the response"""
        response = super(UserViewSet, self).retrieve(request, *args, *kwargs)
        circles = Circle.objects.filter(
            members=request.user,
            membership__is_active=True
        )

        data = {
            'user': response.data,
            'circles': CircleModelSerializer(circles, many=True).data
        }
        response.data = data
        return response


class UserLoginAPIView(APIView):
    """User login API view."""
    pass

    # def post(self, request, *args, **kwargs):
    #     """Handle HTTP POST request."""
    #     serializer = UserLoginSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user, token = serializer.save()
    #     data = {
    #         'user': UserModelSerializer(user).data,
    #         'access_token': token
    #     }
    #     return Response(data, status=status.HTTP_201_CREATED)


# class UserSignUpAPIView(APIView):
#     """User sign up API view."""

#     def post(self, request, *args, **kwargs):
#         """Handle HTTP POST request."""
#         serializer = UserSignUpSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         data = UserModelSerializer(user).data
#         return Response(data, status=status.HTTP_201_CREATED)


# class AccountVerificationAPIView(APIView):
#     """Account verification API view."""

#     def post(self, request, *args, **kwargs):
#         """Handle HTTP POST request."""
#         serializer = AccountVerificationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         data = {'message': 'Congratulation, now go share some rides!'}
#         return Response(data, status=status.HTTP_200_OK)
