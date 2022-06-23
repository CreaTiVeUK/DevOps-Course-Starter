import json
import os
import pytest
import requests
from todo_app import app
from dotenv import load_dotenv, find_dotenv
from flask import current_app

@pytest.fixture
def client():
    try:
        file_path = find_dotenv('.env_test')
        load_dotenv(file_path, override=True)
    except:
        pass
    test_app = app.create_app()
    with test_app.test_client() as client:
        yield client
        
class StubResponse():
    def __init__(self, fake_response_data):
        self.text = json.dumps(fake_response_data)


# Stub replacement for requests.get(url)
def stub(url):
    fake_response_data = None
    if url == f"{current_app.config['TRELLO_URL']}boards/{current_app.config['TRELLO_BOARD_ID']}/lists?key={current_app.config['TRELLO_API_KEY']}&token={current_app.config['TRELLO_API_TOKEN']}&cards=open":
        fake_response_data = [{
            'id': '123abc',
            'name': 'To Do',
            'cards': [{'id': '456', 'name': 'Test card', 'desc': 'Testing descripotion', 'due': "03/15/2022", 'dateLastActivity': "02/15/2022"}]
        }]
        return StubResponse(fake_response_data)
    raise Exception(f'Integration test stub no mock for url "{url}"')


def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, 'get', stub)
    response = client.get('/')
    assert response.status_code == 200
    assert 'Test card' in response.data.decode()

