from rest_framework import serializers
from .models import *

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Invoice

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Payment