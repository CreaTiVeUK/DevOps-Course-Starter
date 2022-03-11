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
    return cards, lists

