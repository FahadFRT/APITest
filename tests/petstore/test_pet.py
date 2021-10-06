import pytest


@pytest.mark.run(order=1)
def test_pet_post(test_conf_pet_post):
    assert test_conf_pet_post.json()['message'] == "1"



@pytest.mark.run(order=2)
def test_pet_get(test_conf_pet_get):
    assert test_conf_pet_get.json()['name'] == "pet001"