from rest_framework import serializers
from rest_framework.validators import UniqueValidator
"""Los serializers son contenedores que nos permiten
    tomar tipos de datos complejos, convertirlos en datos
    nativos de python para después poderlos usar como JSON
    o XML. Son contenedores que amoldan datos para que
    cumplan con las condiciones de los serializers y
    sean llevados a un tipo de estos y después estos
    puedan ser transformados en otra cosa.
    SER EXPLICITO
"""

# Models
from cride.circles.models import Circle


class CircleSerializer(serializers.Serializer):

    name = serializers.CharField()
    slug_name = serializers.SlugField()
    rides_taken = serializers.IntegerField()
    rides_offered = serializers.IntegerField()
    members_limit = serializers.IntegerField()

class CreateCircleSerializer(serializers.Serializer):
    """ Create circle Serializer. """
    name = serializers.CharField(max_length=140)
    slug_name = serializers.SlugField(
        max_length=40,
        validators=[
            UniqueValidator(queryset=Circle.objects.all())
        ]
        )
    about = serializers.CharField(
        max_length=225,
        required=False
    )
    def create(self, data):
        return Circle.objects.create(**data)
