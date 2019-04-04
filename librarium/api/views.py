from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .models import Author
from .models import Publisher

from .serializers import BookSerializer
from .serializers import AuthorSerializer
from .serializers import PublisherSerializer
from .serializers import UserSerializer


class UsersModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for viewing and editing publishers.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    @action(
        detail=False,
        methods=['get']
    )
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class BooksModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for viewing and editing books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)


class AuthorsModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for viewing and editing authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,)


class PublishersModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for viewing and editing publishers.
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (IsAuthenticated,)
