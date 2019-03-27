from rest_framework import viewsets

from .models import Book
from .models import Author
from .models import Publisher

from .serializers import BookSerializer
from .serializers import AuthorSerializer
from .serializers import PublisherSerializer


class BookModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for viewing and editing books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for viewing and editing authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublisherModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for viewing and editing publishers.
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
