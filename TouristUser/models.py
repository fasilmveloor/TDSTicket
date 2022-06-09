from django.db import models
from users.models import User 
from TDSManager.models import TDSUser
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
class TeamMember(models.Model):
    id = models.AutoField(primary_key=True, default=None, auto_created=True)
    name = models.CharField(max_length=100)
    dob = models.DateField(blank=True, null=True)
    vaccination_status = models.CharField(max_length=100, blank=True, null=True)
    vaccination_certificate = models.FileField(upload_to='vaccination/', blank=True, null=True, default='images/default.jpg')

    def __str__(self):
        return self.name

class Ticket(models.Model):
    ticketid = models.AutoField(primary_key=True, default=None, auto_created=True)
    tourist = models.ForeignKey(TouristUser, on_delete=models.CASCADE)
    tds = models.ForeignKey(TDSUser, on_delete=models.CASCADE)
    no_of_Tickets = models.IntegerField(default=0)
    no_of_adults = models.IntegerField(default=0)
    no_of_children = models.IntegerField(default=0)
    total_price = models.FloatField(default=0.0)
    booked_date = models.DateField(auto_now_add=True)
    visiting_date = models.DateField(auto_now_add=False)
    group_image = models.ImageField(upload_to='groupimg/', blank=True, null=True, default='images/default.jpg')
    team_members = models.ManyToManyField(TeamMember, related_name='team_members', blank=True)


    

    