from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from.models import Item
class SriramaSerializers(ModelSerializer):
    class Meta:
        model=Item
        fields= ['Name', 'Cost_per_Item', 'Stock_quantity', 'Volume']