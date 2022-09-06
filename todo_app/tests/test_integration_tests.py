import json
import os
import pytest
import pymongo
import mongomock
from todo_app import app
from dotenv import load_dotenv, find_dotenv
from flask import current_app

from todo_app.data.mongo_db_client import MongoDBClient

@pytest.fixture
def client():
    try:
        file_path = find_dotenv('.env_test')
        load_dotenv(file_path, override=True)
    except:
        pass
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client

class StubResponse():
    def __init__(self, fake_response_data):
        self.text = json.dumps(fake_response_data)

def test_index_page(client):
    mongo_db = MongoDBClient()
    mongo_db.add_item("Test item")
    response = client.get('/')
    assert response.status_code == 200
    assert 'Test item' in response.data.decode()
