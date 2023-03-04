from datetime import date, timedelta

import pytest


""" Фикстура для получения access токена"""

@pytest.fixture
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = "test_user"
    password = "qetuo789"
    birth_date = date.today() - timedelta(days=5000)

    django_user_model.objects.create_user(
        username=username, password=password,
        birth_date=birth_date, role="admin"
    )

    response = client.post(
        "/user/token/",
        {"username": username, "password": password},
        format='json'
    )

    return response.data["access"]
