from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Create your models here.
class UserProfile(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    password = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True, choices=(('M', 'Masculino'), ('F', 'Feminino')))
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
