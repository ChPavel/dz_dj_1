from rest_framework import serializers
from users.models import *


"""Сериализатор для локаций"""

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


"""Сериализатор для создания пользователя"""

class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        many=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop("location", [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for loc_name in self._locations:
            location, _ = Location.objects.get_or_create(name=loc_name)
            user.location.add(location)
        return user


"""Сериализатор для обновления пользователя"""

class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        many=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop("location", [])
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        user = super().save(**kwargs)
        for loc_name in self._locations:
            location, _ = Location.objects.get_or_create(name=loc_name)
            user.location.add(location)
        return user


"""Сериализатор для пользователя при выводе части его полей в одном объявлении"""

class UserAdSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


"""Сериализатор для вывода пользователей списком или по одному со всеми полями"""

class UsersSerializer(serializers.ModelSerializer):
    total_ads = serializers.SerializerMethodField()
    location = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'

    def get_total_ads(self, user):
        return user.ad_set.filter(is_published=True).count()


"""Сериализатор для удаления пользователя"""

class UsersDestroySerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id']


