from django.urls import path

from rest_framework import routers
from rest_framework_jwt import views as jwt_views

from .views import BookModelViewSet
from .views import AuthorModelViewSet
from .views import PublisherModelViewSet


router = routers.DefaultRouter()

router.register(r'books', BookModelViewSet)
router.register(r'authors', AuthorModelViewSet)
router.register(r'publishers', PublisherModelViewSet)

urlpatterns = router.urls


urlpatterns += [
    # Authentication endpoints
    path(
        "auth/jwt/token/obtain/",
        jwt_views.ObtainJSONWebToken.as_view(),
        name="obtain-token",
    ),
    path(
        "auth/jwt/token/refresh/",
        jwt_views.RefreshJSONWebToken.as_view(),
        name="refresh-token",
    ),
    path(
        "auth/jwt/token/verify/",
        jwt_views.VerifyJSONWebToken.as_view(),
        name="verify-token",
    ),
]
