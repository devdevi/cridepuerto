""" Circle model."""

# Django
from django.db import models

# Utilities
from cride.utils.models import CRideModel

#
class Circle(CRideModel):
    """ Circle Model.

    A circle is a private
    """
    name = models.CharField('circle name', max_length=140)
    slug_name = models.CharField(unique=True, max_length=40)

    about = models.CharField('circle description', max_length=255)
    picture = models.ImageField(upload_to='circles/pictures', blank=True, null=True, height_field=None, width_field=None, max_length=None)

    # Members
    members = models.ManyToManyField(
        'users.Users',
        through='circles.Membership',
        through_fields=('circle', 'user')
        )

    # Stats
    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)

    # verified
    verified =models.BooleanField('verified circle',
        default=False,
        help_text="Verified circles are also know as official communities."
    )
    is_public =models.BooleanField('is_public circle',
        default=True,
        help_text="Public circles are listed  in the main page so everyone know about their existence."
    )

    is_limited =models.BooleanField(
        'limited',
        default=False,
        help_text="Limited circles can grow up to a fixed numbers of members."
    )

    members_limit =models.PositiveIntegerField(
        'members limit',
        default=0,
        help_text="If circle is limited, this will be the limit on the number of members."
    )

    def __str__(self):
        """ Return name """
        return self.name

    class Meta(CRideModel.Meta):
        """ Meta class """
        ordering = ['-rides_taken', '-rides_offered']




