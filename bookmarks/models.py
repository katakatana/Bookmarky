from django.db import models
from django.contrib.auth.models import User, AnonymousUser


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Tag(models.Model):
    keyword = models.CharField(max_length=256, unique=True, blank=False)


class Bookmark(models.Model):
    text = models.TextField()

    tags = models.ManyToManyField(Tag)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()



