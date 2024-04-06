from rest_framework import serializers

from mobile.models import Manufacturer, Mobile, MobileCategory

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = '__all__'
        
class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class MobileCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileCategory
        fields = '__all__'