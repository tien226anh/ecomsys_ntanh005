from django.urls import include, path
from rest_framework import routers

from cloth.views import ClothCategoryViewSet, ClothViewSet, ManufacturerViewSet

router = routers.DefaultRouter()
router.register("category", ClothCategoryViewSet)
router.register("manufacturer", ManufacturerViewSet)
router.register("", ClothViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
