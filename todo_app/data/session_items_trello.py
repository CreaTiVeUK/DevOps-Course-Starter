from flask import current_app
from todo_app.data.item import Item
from todo_app.data.list import List
import todo_app.data.configs.logger_settings as logger
import requests
import json
import dateutil.parser

def date_parse(date):
    """
    Parses a date returned from Trello into a suitable format

        Args:
            date: Date returned from Trello
        
        Returns:
            date: Formatted date  
    """
    return dateutil.parser.parse(date).strftime('%m/%d/%Y')

def get_Items_and_Status():
    """
      Get all items from the board.

      Returns:
          items: Nested dictionary of the cards, or None if no cards were found
    """
    url = f"{current_app.config['TRELLO_URL']}boards/{current_app.config['TRELLO_BOARD_ID']}/lists?key={current_app.config['TRELLO_API_KEY']}&token={current_app.config['TRELLO_API_TOKEN']}&cards=open"
    response = requests.get(url)
    response_json = json.loads(response.text)
    cards, lists = [], []
    for list in response_json:
        lists.append(List(list['id'], list['name']))
        for card in list['cards']:         
            cards.append(Item(
                card['id'],
                card['name'],
                card['desc'],
                card['due'] if card['due'] is None else date_parse(card['due']),
                date_parse(card['dateLastActivity']),
                list['name'],
                list['id'])
            )
    return cards

def create_Card(list_name, card_name):
    """
        Create a card as part of a list with the specified list name and card name.

    Args:
        list_name: List name.
        card_name: Card name.
    """
    card = {
        "name": card_name,
        "idBoard": current_app.config['TRELLO_BOARD_ID'],
        "idList": get_List_ID(list_name),
        "idMembers": ""
    }
    url = f"{current_app.config['TRELLO_URL']}cards?key={current_app.config['TRELLO_API_KEY']}&token={current_app.config['TRELLO_API_TOKEN']}"
    requests.post(url, card)

def move_Card(to_list, card_id):
    """
    Move a card into the specified list name.

    Args:
        to_list: List to move the card to.
        card_id: ID of the card.
    """
    url = f"{current_app.config['TRELLO_URL']}cards/{card_id}?key={current_app.config['TRELLO_API_KEY']}&token={current_app.config['TRELLO_API_TOKEN']}"
    card = {
        "idList": get_List_ID(to_list)
    }
    requests.put(url, card)

def update_item_description(card_id, description):
    """
    Update a card's description.

    Args:
        card_id: ID of the card.
        description: Description of the card.
    """
    url = f"{current_app.config['TRELLO_URL']}cards/{card_id}?key={current_app.config['TRELLO_API_KEY']}&token={current_app.config['TRELLO_API_TOKEN']}"
    card = {
        "desc": description
    }
    requests.put(url, card)

def update_item_due_date(card_id, due):
    """
    Update a card's due date.

    Args:
        card_id: ID of the card.
        due: Due date of the card.
    """
    url = f"{current_app.config['TRELLO_URL']}cards/{card_id}?key={current_app.config['TRELLO_API_KEY']}&token={current_app.config['TRELLO_API_TOKEN']}"
    card = {
        "due": due
    }
    requests.put(url, card)

def get_List_ID(list_name):
    """
        Get list's ID from the specified list name.

        Args:
            list_name: List name.

        Returns:
            List's ID, or None if no ID matches the specified name.
    """
    url = f"{current_app.config['TRELLO_URL']}boards/{current_app.config['TRELLO_BOARD_ID']}/lists?key={current_app.config['TRELLO_API_KEY']}&token={current_app.config['TRELLO_API_TOKEN']}"
    response = requests.get(url)
    response_json = json.loads(response.text)
    for list in response_json:
        if list['name'] == list_name:
            return list['id']
