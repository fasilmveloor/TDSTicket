from django.db import models
from users.models import User
# Create your models here.
class TDType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.type

class TDSUser(models.Model):
    tdid = models.AutoField(primary_key = True, default=None, auto_created=True)
    user = models.OneToOneField(User,related_name='tds', on_delete=models.CASCADE)
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

class Announcements(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    tds = models.ForeignKey(TDSUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title