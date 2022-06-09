from django.db import models
from users.models import User 
# Create your models here.
class TouristUser(models.Model):
    user = models.OneToOneField(User,related_name='tourist', on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True, default='images/default.jpg')
    is_vaccinated = models.BooleanField(default=False)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name