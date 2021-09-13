"""Circle serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from cride.circles.models import Circle
from rest_framework.exceptions import MethodNotAllowed

class CircleModelSerializer(serializers.ModelSerializer):
    """Circle model serializer."""

    members_limit = serializers.IntegerField(
        required=False,
        min_value=10,
        max_value=1200
    )
    is_limited = serializers.BooleanField(default=False)

    class Meta:
        """Meta class."""

        model = Circle
        fields = (
            'id', 'name', 'slug_name',
            'about', 'picture',
            'rides_offered', 'rides_taken',
            'verified', 'is_public',
            'is_limited', 'members_limit'
        )
        read_only_fields =(
            'is_public',
            'verified',
            'rides_offered'
        )
    def validate(self, data):
        """Ensure both members limit and is limited are present."""
        method = self.context['request'].method

        if method == 'POST':
            members_limit = data.get('members_limit', None)
            is_limited = data.get('is_limited', False)

            if bool(members_limit) ^ is_limited:
                raise serializers.ValidationError('If there is members_limit or is_limited both need to exist.')

        return data
