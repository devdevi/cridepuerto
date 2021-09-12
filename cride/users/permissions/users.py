# Django rest framework
from rest_framework.permissions import BasePermission
# Models
from cride.users.models import User

class IsAccountOwner(BasePermission):
    """Allow acces only to objects owned by the requesting user"""

    def has_object_permission(self, request, view, obj):
        """Verified user a have a memebership in the obj"""
        return request.user == obj
