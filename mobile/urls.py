from django.urls import include, path
from rest_framework import routers

from mobile.views import ManufacturerViewSet, MobileCategoryViewSet, MobileViewSet

router = routers.DefaultRouter()
router.register("manufacturer", ManufacturerViewSet, basename="manufacturer")
router.register("category", MobileCategoryViewSet, basename="category")
router.register("", MobileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]