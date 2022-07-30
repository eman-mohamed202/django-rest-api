from dataclasses import fields
from operator import itemgetter
from pyexpat import model
from rest_framework import serializers
from base.models import Item




class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'