from unicodedata import name
import requests
import dotenv
import os
import json

dotenv.load_dotenv()

api_url = os.getenv('TRELLO_URL')
api_key = os.getenv('TRELLO_API_KEY')
api_token = os.getenv('TRELLO_API_TOKEN')
board_id = os.getenv('TRELLO_BOARD_ID')

def get_Cards():
  url = f"{api_url}boards/{board_id}/lists?key={api_key}&token={api_token}&cards=open"
  response = requests.get(url)
  response_json = json.loads(response.text)
  cards = []
  for list in response_json:
    if list['name'] == 'To Do':
      for card in list['cards']:
        cards.append(card['name'])
  return cards


def create_Card(name):
  card = {
    "name": name, 
    "idBoard": "61c9efb12a4989214a75b4a5", 
    "idList": "61c9efb12a4989214a75b4a8"
  }
  url = f"{api_url}cards?key={api_key}&token={api_token}"
  requests.post(url, card)


print(get_Cards())
create_Card("test3")
