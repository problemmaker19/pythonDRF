from django.db import models

from users.models import CustomUser


class Contacts(models.Model):
    github = models.CharField(max_length=8000)
    vk = models.CharField(max_length=8000)
    facebook = models.CharField(max_length=8000)
    instagram = models.CharField(max_length=8000)
    twitter = models.CharField(max_length=8000)
    website = models.CharField(max_length=8000)
    youtube = models.CharField(max_length=8000)
    mainLink = models.CharField(max_length=8000)

    def __str__(self):
        return self.mainLink


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    contacts = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.user}'
