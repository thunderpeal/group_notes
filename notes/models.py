from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

from django.forms import inlineformset_factory


class NoteGroup(models.Model):
    id = models.SmallAutoField(primary_key=True)
    group_name = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.group_name


class CustomUser(AbstractUser):
    phone_number = models.CharField(unique=True, max_length=10, null=True, blank=True)
    note_group = models.ForeignKey(NoteGroup, on_delete=models.DO_NOTHING, null=True, blank=True)
    group_admin = models.BooleanField(default=False)

    #objects = CustomUserManager()


class SNote(models.Model):
    id = models.SmallAutoField(primary_key=True)
    heading = models.CharField(max_length=25, blank=True, null=True)
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='noteAuthor',
                               blank=True, null=True)
    to_whom = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='toWhom')
    is_for_group = models.BooleanField(default=False)

    class Meta:
        ordering = ['datetime']

    def __str__(self):
        if self.heading:
            return f'{self.heading}'
        return 'Записка №' + str(self.id)


class SComment(models.Model):
    id = models.SmallAutoField(primary_key=True)
    note = models.ForeignKey(SNote, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    message = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['datetime']