from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Book(BaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)


class Publisher(BaseModel):
    name = models.CharField(max_length=50)
