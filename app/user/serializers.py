from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        # Model to base serializer on
        model = get_user_model()
        # Fields to include and convert to and from JSON
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        # Here we are overiding the built in create function
        return get_user_model().objects.create_user(**validated_data)
