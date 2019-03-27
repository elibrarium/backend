from django.urls import path
from django.urls import include

from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
    path(
        '',
        include(router.urls)
    ),
    path(
        'api/v1/',
        include('api.urls'),
    ),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
]
