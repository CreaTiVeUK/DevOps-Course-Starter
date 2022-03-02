from todo_app.config.credentials import *
from todo_app.data.list import List
import requests


class Item:

    def __init__(self, id, name, description, due, list_name, list_id):
        self.id = id
        self.name = name
        self.description = description
        self.due = due
        self.list_name = list_name
        self.list_id = list_id

    def create_Card(list_name, card_name):
        """
            Create a card as part of a list with the specified list name and card name.

        Args:
            list_name: List name.
            card_name: Card name.
        """
        card = {
            "name": card_name,
            "idBoard": "61c9efb12a4989214a75b4a5",
            "idList": List.get_List_ID(list_name),
            "idMembers": ""
        }
        url = f"{api_url}cards?key={api_key}&token={api_token}"
        requests.post(url, card)

    def move_Card(to_list, card_id):
        """
        Move a card into the specified list name.

        Args:
            to_list: List to move the card to.
            card_id: ID of the card.
        """
        url = f"{api_url}cards/{card_id}?key={api_key}&token={api_token}"
        card = {
            "idList": List.get_List_ID(to_list)
        }
        requests.put(url, card)

    def update_item_description(card_id, description):
        """
        Update a card's description.

        Args:
            card_id: ID of the card.
            description: Description of the card.
        """
        url = f"{api_url}cards/{card_id}?key={api_key}&token={api_token}"
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
        url = f"{api_url}cards/{card_id}?key={api_key}&token={api_token}"
        card = {
            "due": due
        }
        requests.put(url, card)
