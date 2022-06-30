from rest_framework import routers
from .views import CleaningsViewSet, CitiesViewSet
from django.urls import path
from django.urls.conf import include, re_path

router = routers.DefaultRouter()
router.register(r'cleanings', CleaningsViewSet)
router.register(r'cities', CitiesViewSet)

urlpatterns = [
    re_path(r'', include(router.urls)),
]