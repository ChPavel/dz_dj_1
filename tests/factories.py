from datetime import date, timedelta

import factory.django

from ads.models import Ad, Category
from users.models import User


""" Фабрика для создания категорий"""

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('name')
    slug = factory.Faker('ean', length=8)


""" Фабрика для создания пользователей"""

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    birth_date = date.today() - timedelta(days=5000)


""" Фабрика для создания объявлений"""

class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = factory.Faker('name')
    category_id = factory.SubFactory(CategoryFactory)
    author_id = factory.SubFactory(UserFactory)
    price = 1400
