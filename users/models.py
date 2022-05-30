from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class User(AbstractUser):
    is_tds = models.BooleanField(default=False)
    is_tourist = models.BooleanField(default=False)

    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class TDType(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.type

class TDSUser(models.Model):
    user = models.OneToOneField(User,related_name='tds', on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    opening_time = models.TimeField(blank=True, null=True)
    closing_time = models.TimeField(blank=True, null=True)
    holydays = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    ticket_fair = models.FloatField(blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    visitor_min_age = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    type = models.ForeignKey(TDType, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class TouristUser(models.Model):
    user = models.OneToOneField(User,related_name='tourist', on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True, default='images/default.jpg')
    is_vaccinated = models.BooleanField(default=False)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    