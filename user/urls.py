from django.urls import include, path
from rest_framework import routers

from user.views import GroupViewSet, RegisterView, UserViewSet

router = routers.DefaultRouter()
# router.register("register", RegisterView, basename="register")
router.register("group", GroupViewSet)
router.register("", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
