from rest_framework import viewsets

from .models import Author
from .serializers import AuthorSerializer


class AuthorModelViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
