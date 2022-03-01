from todo_app.config.credentials import *
from todo_app.data.item import Item
from todo_app.data.list import List
import requests
import json


def get_Items_and_Status():
    """
      Get all items from the board.

      Returns:
          items: Nested dictionary of the cards, or None if no cards were found
    """
    url = f"{api_url}boards/{board_id}/lists?key={api_key}&token={api_token}&cards=open"
    response = requests.get(url)
    response_json = json.loads(response.text)
    cards, lists = [], []
    for list in response_json:
        lists.append(List(list['id'], list['name']))
        for card in list['cards']:
            cards.append(Item(card['id'], card['name'],
                         list['name'], list['id']))
    return cards, lists
