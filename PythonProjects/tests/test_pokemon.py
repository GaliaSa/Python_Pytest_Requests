import requests
import pytest


URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "072d55fa96f455d4523c0d01e2d5ccc3"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}
TRAINER_ID = "27555"


def test_status_code():
    response = requests.get(url=f"{URL}/pokemons", params={"trainer_id": TRAINER_ID})
    assert response.status_code == 200


def test_status_code_2():
    response_get = requests.get(url=f"{URL}/trainers")
    assert response_get.status_code == 200


def test_trainer_name():
    response_name = requests.get(
        url=f"{URL}/trainers", params={"trainer_id": TRAINER_ID}
    )
    assert response_name.json()["data"][0]["trainer_name"] == "Saiga"


@pytest.mark.parametrize("key, value", [("trainer_name", "Saiga"), ("id", "27555")])
def test_parametrize(key, value):
    response_parametrize = requests.get(
        url=f"{URL}/trainers", params={"trainer_id": TRAINER_ID}
    )
    assert response_parametrize.json()["data"][0][key] == value
