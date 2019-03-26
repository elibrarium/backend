from rest_framework import routers

from .views import AuthorModelViewSet


router = routers.SimpleRouter()
router.register(r'authors', AuthorModelViewSet)
urlpatterns = router.urls
