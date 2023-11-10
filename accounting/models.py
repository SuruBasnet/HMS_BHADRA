from django.db import models
from frontdesk.models import Guest

# Create your models here.
invoice_status = [('Paid','Paid'),('Unpaid','Unpaid')]

class Invoice(models.Model):
    guest = models.ForeignKey(Guest,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=300)
    amount = models.IntegerField()
    status = models.CharField(max_length=300,choices=invoice_status)

class Payment(models.Model):
    invoice = models.OneToOneField(Invoice,on_delete=models.CASCADE)
    amount = models.IntegerField()
