from django.shortcuts import render
from rest_framework import viewsets

from cloth.models import Cloth, ClothCategory, Manufacturer
from cloth.serializers import ClothCategorySerializer, ClothSerializer
from mobile.serializers import ManufacturerSerializer


# Create your views here.
class ClothViewSet(viewsets.ModelViewSet):
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer


class ClothCategoryViewSet(viewsets.ModelViewSet):
    queryset = ClothCategory.objects.all()
    serializer_class = ClothCategorySerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
