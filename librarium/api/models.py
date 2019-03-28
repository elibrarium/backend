from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel


class Author(TimeStampedModel):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(
        max_length=100,
    )
    last_name = models.CharField(
        max_length=100,
    )
    middle_name = models.CharField(
        max_length=100,
        blank=True,
    )
    photo = models.ImageField(
        upload_to='authors',
        default='',
    )


class Publisher(TimeStampedModel):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=100
    )
    description = models.TextField(
        max_length=600
    )
    logo = models.ImageField(
        upload_to='publishers',
        default='',
    )


class Book(TimeStampedModel):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=150
    )
    description = models.TextField(
        max_length=600
    )
    upload = models.FileField(
        upload_to='books/'
    )
    cover = models.ImageField(
        upload_to='books/',
        default='',
    )
    published_date = models.DateField()
    authors = models.ManyToManyField(
        Author,
    )
    publisher = models.ManyToManyField(
        Publisher,
    )
