from rest_framework import serializers

from ads.models import Selection
from ads.serializers.serislizers_ad import AdSerializer

"""Сериализатор для подборок"""
class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id", "name"]


"""Сериализатор для подборок по умолчанию"""
class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"


"""Сериализатор для одной подборки"""
class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdSerializer(many=True)
    class Meta:
        model = Selection
        fields = "__all__"
