# todos/serializers.py
from rest_framework import serializers
from .models import myresume


class Serializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = myresume