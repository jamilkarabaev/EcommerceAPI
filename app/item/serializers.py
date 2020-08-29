from rest_framework import serializers
from core import models

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = ['id', 'seller', 'title', 'description', 'category', 'price', 'in_stock', 'image', 'uploaded_date', 'in_stock']
        read_only_fields = ['id', 'seller', 'uploaded_date']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = ['id', 'user', 'item', 'stars', 'review']
        read_only_fields = ['id', 'user']
