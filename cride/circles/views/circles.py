"""Circle views."""

# Django REST Framework
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import MethodNotAllowed
# Serializers
from cride.circles.serializers import CircleModelSerializer

# Models
from cride.circles.models import Circle, Membership
from cride.permissions import IsCircleAdmin


class CircleViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Circle view set."""

    lookup_field = 'slug_name'
    serializer_class = CircleModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Restrict list to public.only"""

        queryset = Circle.objects.all()
        if self.action == 'list':
            return queryset.filter(is_public=True)
        return queryset

    def get_permission(self):
        """Assing permission based on actions"""
        permissions =[IsAuthenticated]
        if self.action == ['update', 'partial_update']:
            permissions.append(IsCircleAdmin)
        return [p() for p in permissions]


    def perform_create(self, serializer):
        """Assing circle admin"""
        circle = serializer.save()
        user = self.request.user
        profile = user.profile
        Membership.objects.create(
            user=user,
            profile=profile,
            circle=circle,
            is_admin=True,
            remaining_invitations=10
        )


    def destroy(self, request, pk=None):
        raise MethodNotAllowed('DELETE')
