from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=300)

class Food(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(null=True)
    menu = models.ForeignKey(Menu,on_delete=models.SET_NULL,null=True)