from django.db import models
from management.models import Room

# Create your models here.
class Guest(models.Model):
    full_name = models.CharField(max_length=300)
    contact = models.IntegerField()
    address = models.CharField(max_length=300)
    work = models.CharField(max_length=300)
    email = models.EmailField()
    reference_contact = models.IntegerField(null=True)

class GuestRoom(models.Model):
    guest = models.ForeignKey(Guest,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)