from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = "__all__"


class GroupSerializer(serializers.Serializer):
    class Meta:
        model = Group
        fields = "__all__"


class RegisterSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        # extra_kwargs = {"password": {"write_only": True}}
