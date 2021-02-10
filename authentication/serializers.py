from rest_framework import serializers
from rest_framework import status
from rest_framework.exceptions import ValidationError, AuthenticationFailed

from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


from .utils import get_tokens_for_user

# Getting Django user model
User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration
    """

    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=150)
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(min_length=4, max_length=55, write_only=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password")

    def validate(self, attrs):
        username = attrs.get("username")
        user = self.Meta.model.objects.filter(username=username).exists()

        if user:
            raise ValidationError(
                f"User with username: {username} already exists.",
                code=status.HTTP_400_BAD_REQUEST,
            )
        return super().validate(attrs)

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login
    """

    username = serializers.CharField(max_length=150)
    password = serializers.CharField(min_length=4, max_length=55, write_only=True)

    def validate(self, attrs):
        username = attrs.get("username", "")
        password = attrs.get("password", "")
        user = auth.authenticate(username=username, password=password)
        if user:
            attrs = get_tokens_for_user(user)
            return attrs
        else:
            raise AuthenticationFailed(detail="Credentials are invalid. Try again...")
