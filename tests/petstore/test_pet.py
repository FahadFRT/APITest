

@pytest.mark.run(order=6)
def test_pet_get(test_conf_pet_get):
    assert test_conf_pet_get.json()['name'] == "doggie"