from rest_framework import serializers
from users.models import *


"""Сериализатор для создания пользователя"""
class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        many=True,
        slug_field='name'
    )

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop("location", [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        for loc_name in self._locations:
            location, _ = Location.objects.get_or_create(name=loc_name)
            user.location.add(location)
        return user

    class Meta:
        model = User
        fields = '__all__'


"""Сериализатор для пользователя при выводе одного объявления"""
class UserAdSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


"""Сериализатор для локаций"""
class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'