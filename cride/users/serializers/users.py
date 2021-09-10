"""Users Serializers"""

# Django
from time import timezone
from cride.users.models.users import User
from django.contrib.auth import authenticate, password_validation
from django.core.validators import RegexValidator
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

# Django Rest Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator


# Utils
import jwt
from datetime import timedelta
from django.utils import timezone

# Models
from cride.users.models import User, Profile


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer"""

    class Meta:
        """Meta Class"""

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number'
        )


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.

    Handle the login request data.
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=4, max_length=42)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')

        if not user.is_verified:
            raise serializers.ValidationError('Account is not active yet')
        self.context["user"] = user
        return data

    def create(self, data):
        """Generate or retrive new token"""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


class UserSignUpSerializer(serializers.Serializer):
    """User SingUp serializer.

    Handle sign up data validation and user/profile creation
    """

    email = serializers.EmailField(validators=[
        UniqueValidator(queryset=User.objects.all())
    ])
    username = serializers.CharField(min_length=4,
                                     max_length=20,
                                     validators=[
                                         UniqueValidator(queryset=User.objects.all()),

                                     ])

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = serializers.CharField(validators=[phone_regex], max_length=17)

    # Password
    password = serializers.CharField(min_length=4, max_length=42)
    password_confirmation = serializers.CharField(min_length=4, max_length=42)

    # Name

    first_name = serializers.CharField(min_length=1, max_length=42)
    last_name = serializers.CharField(min_length=4, max_length=42)

    def validate(self, data):
        """Verified password match."""

        passwd = data["password"]
        passwd_confirmation = data["password_confirmation"]

        if passwd != passwd_confirmation:
            raise serializers.ValidationError("Password don't match.")
        # Validar contraseño con django
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Handle user and profile creation"""

        data.pop('password_confirmation')
        user = User.objects.create_user(**data, is_verified=False)
        Profile.objects.create(user=user)
        self.send_confirmation_email(user)
        return user

    def send_confirmation_email(self, user):
        """ Send account verification link to given user. """
        verification_token = self.gen_verification_token(user)

        subject = f"Welcome {user.username}"
        from_email = 'Comparte Ride <noreply@comparteride.com>'

        text_content = 'This is an important message.'
        content = render_to_string('email/users/account_verification.html', {
             'token': verification_token, 'user': user})
        msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
        msg.attach_alternative(content, "text/html")
        msg.send()
        pass

    def gen_verification_token(self, user):
        """Create JWI token that the user can use to verified account """
        exp_date = timezone.now() + timedelta(days=3)
        payload = {
            'user': user.username,
            'exp': int(exp_date.timestamp()),
            'type': 'email_confirmation'
        }

        encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        return encoded_jwt


class AccountVerificationSerializer(serializers.Serializer):
    """Account verification serializer"""

    token = serializers.CharField()

    def validate(self, data):
        """Validate token is valid."""
        try:
            payload = jwt.decode(data['token'], settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Verification link has expired.')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Invalid token')

        else:
            if payload['type'] != 'email_confirmation':
                raise serializers.ValidationError('Invalid token :/:')
            self.context['payload'] = payload
            return data


    def save(self):
        """Update users verified status"""
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.is_verified = True
        user.save()

