from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import * 

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = "__all__"

class ClientsSMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientsSMS
        fields = "__all__"

class BillingSerializer(ModelSerializer):
    class Meta:
        model = Billing
        fields = "__all__"
        
class CustomersSerializer(ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"