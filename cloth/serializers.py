from rest_framework import serializers

from cloth.models import Cloth, ClothCategory, Manufacturer


class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = "__all__"


class ClothCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothCategory
        fields = "__all__"


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"
