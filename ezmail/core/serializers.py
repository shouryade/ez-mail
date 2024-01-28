from rest_framework import serializers
from rest_framework.response import Response
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
