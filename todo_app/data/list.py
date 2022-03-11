from flask import current_app
import requests
import json


class List:

    def __init__(self, id, name):
        self.id = id
        self.name = name

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
