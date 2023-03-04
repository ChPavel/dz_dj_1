import pytest


""" Тест создания объявления"""

@pytest.mark.django_db
def test_ad_create(client, user, category, access_token):
    data = {
        "name": "Стол тестовый",
        "price": 2600,
        "description": "Стол тестовый почти огонь",
        "is_published": False,
        "author_id": user.pk,
        "category_id": category.pk
    }

    expected_data = {
            "id": 1,
            "is_published": False,
            "name": "Стол тестовый",
            "price": 2600,
            "description": "Стол тестовый почти огонь",
            "image": None,
            "author_id": 1,
            "category_id": 1
    }
    response = client.post(
        '/ad/',
        data,
        format='json',
        HTTP_AUTHORIZATION="Bearer " + access_token
    )
    assert response.status_code == 201
    assert response.data == expected_data
