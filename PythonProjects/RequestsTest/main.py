import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "072d55fa96f455d4523c0d01e2d5ccc3"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}
TRAINER_ID = 27555
body_creation = {"name": "FromPyton", "photo_id": -1}

body_namechange = {"pokemon_id": "290788", "name": "Newname", "photo_id": 2}

body_catch = {"pokemon_id": "290788"}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creation)
print(response_create.text)


"""response_namechange = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_namechange)
print(response_namechange.text)"""

"""response_catch = requests.post(
    url=f"{URL}/trainers/add_pokeball", headers=HEADER, json=body_catch
)
print(response_catch.text)"""

message = response_create.json()['message']
print(message)
