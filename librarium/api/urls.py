from rest_framework import routers

from .views import BookModelViewSet
from .views import AuthorModelViewSet
from .views import PublisherModelViewSet


router = routers.DefaultRouter()

router.register(r'books', BookModelViewSet)
router.register(r'authors', AuthorModelViewSet)
router.register(r'publishers', PublisherModelViewSet)

urlpatterns = router.urls
