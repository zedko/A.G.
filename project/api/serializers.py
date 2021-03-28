from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Only username and email from standard User model
    """
    class Meta:
        model = User
        fields = ['username', 'email']
