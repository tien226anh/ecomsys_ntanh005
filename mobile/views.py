from django.shortcuts import render
from rest_framework import viewsets

from mobile.models import Manufacturer, Mobile, MobileCategory
from mobile.serializers import ManufacturerSerializer, MobileCategorySerializer, MobileSerializer

# Create your views here.
class MobileViewSet(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    
class MobileCategoryViewSet(viewsets.ModelViewSet):
    queryset = MobileCategory.objects.all()
    serializer_class = MobileCategorySerializer