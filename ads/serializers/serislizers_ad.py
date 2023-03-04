from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from ads.models import *
from ads.validators import not_published
from users.models import User
from users.serializers import UserAdSerializer


"""Сериализатор для объявлений по умолчанию"""
class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


"""Сериализатор для создания объявления объявлений"""
class AdCreateSerializer(serializers.ModelSerializer):
    is_published = serializers.BooleanField(validators=[not_published])
    class Meta:
        model = Ad
        fields = '__all__'


"""Сериализатор для объявлений списком"""
class AdListSerializer(serializers.ModelSerializer):
    author_id = SlugRelatedField(slug_field='username', queryset=User.objects.all())
    category_id = SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = '__all__'


"""Сериализатор для одного объявления"""
class AdDetailSerializer(serializers.ModelSerializer):
    author_id = UserAdSerializer()
    # author_id = SlugRelatedField(slug_field='username', queryset=User.objects.all())
    category_id = SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = '__all__'
