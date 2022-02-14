from traceback import print_tb
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


def get_Lists_and_Cards():
  """
    Get all cards from the board.

    Returns:
        cards: Nested dictionary of the cards, or None if no cards were found
  """
  url = f"{api_url}boards/{board_id}/lists?key={api_key}&token={api_token}&cards=open"
  response = requests.get(url)
  response_json = json.loads(response.text)
  cards = {}
  lists = {}
  for list in response_json:
    lists[list['name']] = {'list_id': list['id']}
    for card in list['cards']:
      cards[card['name']] = {'card_id': card['id'], 'list_name': list['name'], 'list_id': list['id']}
  return cards,lists


def get_List_ID(list_name):
  """
    Get list's ID from the specified list name.

    Args:
        list_name: List name.

    Returns:
        List's ID, or None if no ID matches the specified name.
  """
  url = f"{api_url}boards/{board_id}/lists?key={api_key}&token={api_token}"
  response = requests.get(url)
  response_json = json.loads(response.text)
  for list in response_json:
    if list['name'] == list_name:
      return list['id']
  

def create_Card(list_name, card_name):
  """
    Create a card as part of a list with the specified list name and card name.

    Args:
        list_name: List name.
        card_name: Card name.

    Returns:
        card: Saved card.
  """
  card = {
    "name": card_name, 
    "idBoard": "61c9efb12a4989214a75b4a5", 
    "idList": get_List_ID(list_name),
    "idMembers": ""
  }
  url = f"{api_url}cards?key={api_key}&token={api_token}"
  requests.post(url, card)


def move_Card(to_list, card_id):
  """
    Move a card into the specified list name.

    Args:
        to_list: List to move the card to.
        card_name: Name of the card.

    Returns:
        card: The moved card.
  """
  url = f"{api_url}cards/{card_id}?key={api_key}&token={api_token}"
  card = {
    "idList": get_List_ID(to_list)
  }
  requests.put(url, card)

cards,lists = get_Lists_and_Cards()
#print(cards["test4"]['card_id'])
#print(lists["To Do"]['list_id'])
#print(get_Card_ID("test4"))
create_Card("To Do", "test6")
move_Card("Doing", cards['test6']['card_id'])
#print(move_Card('Done','test4'))
