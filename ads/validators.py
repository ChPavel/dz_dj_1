from rest_framework import serializers


""" Валидатор для поля is_published модели Ad"""

def not_published(value):
    if value:
        raise serializers.ValidationError(f"Значение поля is_published при создании объявления не может быть True")
