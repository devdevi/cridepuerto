"""Users URLs."""

# # Django
# from django.urls import path

# # Views
# from cride.users.views import (
#     AccountVerificationAPIView,
#     UserLoginAPIView,
#     UserSignUpAPIView
# )

# urlpatterns = [
#     path('users/login/', UserLoginAPIView.as_view(), name='login'),
#     path('users/signup/', UserSignUpAPIView.as_view(), name='signup'),
#     path('users/verify/', AccountVerificationAPIView.as_view(), name='verify'),
# ]
# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import users as user_views

router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
