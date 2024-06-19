import datetime
from typing import Dict
from fastapi.testclient import TestClient
from main import app
import json
from schemas import ProdIn,ProdDict
from main import add_prod
from tasks import task_add_prod, task_get_prod, task_update_prod, task_delete_prod, task_get_prods, crud_get_prod_name


client = TestClient(app)


def test_task_add_prod():

    payload = {
        "name": "ldiniz456",
        "pricing": {
            "amount": 100,
            "currency": "BRL"
        },
        "description": "foo@domain.com",
        "availability": {
            "quantity": 50,
            "timestamp": "2024-06-12T12:00:00Z"
        },
        "category": "000000000"
        }

    payload_update = {
            "name": "ldini46",
            "pricing": {
                "amount": 100,
                "currency": "BRL"
            },
            "description": "foo@domain.com",
            "availability": {
                "quantity": 49,
                "timestamp": "2024-06-12T12:00:00Z"
            },
            "category": "000000000"
            }

    response = task_add_prod(payload)
    content = response['data'].dict()
    assert content['name'] == 'ldiniz456'
    assert content['pricing'] == str(payload['pricing'])
    assert content['availability'] == str(payload['availability'])
    assert content["category"] == "000000000"

    response = task_add_prod(payload)
    assert response == {
        'message': 'prod already exists ', 'status_code': '403'}

    response = client.get("/prods")
    content = response.json()['data'][0]['id']
    assert response.json()['data'][0]['name'] == 'ldiniz456'
    assert response.json()['data'][0]['pricing'] == str(payload['pricing'])
    assert response.json()['data'][0]['availability'] == str(payload['availability'])
    assert response.json()['data'][0]['category'] == "000000000"   

    response = task_delete_prod(int(content))
    assert response == {'message': 'prod deleted'}

    
