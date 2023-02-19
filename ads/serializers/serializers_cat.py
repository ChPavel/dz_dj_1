from rest_framework import serializers
from ads.models import Category


"""Сериализатор для категорий"""
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
