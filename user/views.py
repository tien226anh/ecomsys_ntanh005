from django.shortcuts import render
from django.contrib.auth.models import User, Group, AbstractBaseUser
from rest_framework import viewsets, views, response, status

from user.serializers import GroupSerializer, UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RegisterView(views.APIView):
    def post(self, request):
        data = request.data
        user = User.objects.create_user(
            data["username"], data["email"], data["password"]
        )
        user.save()
        return response({"message": "User created"}, status=status.HTTP_201_CREATED)
