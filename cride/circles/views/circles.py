# Django Fest Framework

from rest_framework import viewsets

# Models
from cride.circles.models import Circle

# Ser
from cride.circles.serializers import CircleModelSerializer

class CircleViewSet(viewsets.ModelViewSet):
    """Circle view set."""

    queryset = Circle.objects.all()
    serializer_class = CircleModelSerializer
