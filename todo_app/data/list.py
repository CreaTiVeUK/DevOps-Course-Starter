from todo_app.config.credentials import *
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
        url = f"{api_url}boards/{board_id}/lists?key={api_key}&token={api_token}"
        response = requests.get(url)
        response_json = json.loads(response.text)
        for list in response_json:
            if list['name'] == list_name:
                return list['id']
