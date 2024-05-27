import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '1667dbb954b9536531a79b602520b2fe'
HEADER = {'Content-Type' : 'application/json','trainer_token':TOKEN}
TRAINER_ID = '4275'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_part_response():
    response_get = requests.get(url = f'{URL}/trainers', params={'trainer_id': 4275})
    assert response_get.json()["data"][0]['trainer_name'] == 'Scooby'


    
    
     