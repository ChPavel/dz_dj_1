import pytest

from ads.serializers.serislizers_ad import AdDetailSerializer


""" Тест детального отображения объявления"""

@pytest.mark.django_db
def test_ad_retrieve(client, ad, access_token):
    response = client.get(f"/ad/{ad.pk}/", HTTP_AUTHORIZATION="Bearer " + access_token)
    assert response.status_code == 200
    assert response.data == AdDetailSerializer(ad).data
