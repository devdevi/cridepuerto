# Django rest framework
from rest_framework.permissions import BasePermission

class IsAccountOwner(BasePermission):
    """Allow access only to objects owned by the requesting user"""

    def has_object_permission(self, request, view, obj):
        """Verified user a have a memebership in the obj"""
        return request.user == obj
