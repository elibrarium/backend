from django.db import models
# from django.conf.settings import AUTH_USER_MODEL as User


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class Author(TimeStampedModel):
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
    userpic = models.ImageField(
        upload_to='userpics'
    )


class Publisher(TimeStampedModel):
    name = models.CharField(
        max_length=100
    )
    description = models.TextField(
        max_length=600
    )


class Book(TimeStampedModel):
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
        upload_to='books/'
    )
    published_date = models.DateField()
    authors = models.ManyToManyField(
        Author,
    )
    publisher = models.ManyToManyField(
        Publisher,
    )
