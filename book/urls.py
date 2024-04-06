from django.urls import include, path
from rest_framework import routers

from book.views import AuthorViewSet, BookCategoryViewSet, BookViewSet, PublisherViewSet

router = routers.DefaultRouter()
router.register("publisher", PublisherViewSet, basename="publisher")
router.register("category", BookCategoryViewSet, basename="category")
router.register("author", AuthorViewSet, basename="author")
router.register("", BookViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
