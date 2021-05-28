from django.db.models import fields
from rest_framework import serializers
from .models import funds_info

class funds_Serializer(serializers.ModelSerializer):
    class Meta:
        model = funds_info
        fields = ['code','name']