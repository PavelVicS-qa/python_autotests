import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '1667dbb954b9536531a79b602520b2fe'
HEADER = {'Content-Type' : 'application/json','trainer_token':TOKEN}
body_registration = {
    "trainer_token" : TOKEN,
    "email" : "panda1@yandex.ru",
    "password" : "LoveQaStudio999"

}
body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "generate",
    "photo": "generate"
}

body_change = {
    "pokemon_id": "28330",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_catch_pokemon = {
    "pokemon_id": "28330"
}

response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)

response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_change_name = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change_name.text)

response_catch_pokemon = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch_pokemon)
print(response_catch_pokemon.text)













