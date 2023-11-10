from django.db import models

# Create your models here.
room_status = [('Available','Available'),('Unavailable','Unavailable'),('In use','In use')]

class RoomType(models.Model):
    name = models.CharField(max_length=300)

class Room(models.Model):
    room_no = models.CharField(max_length=300)
    floor = models.CharField(max_length=300)
    description = models.TextField(null=True)
    bed_count = models.IntegerField()
    status = models.CharField(max_length=300,choices=room_status)
    type = models.ForeignKey(RoomType,on_delete=models.SET_NULL,null=True)

class Service(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(null=True)
