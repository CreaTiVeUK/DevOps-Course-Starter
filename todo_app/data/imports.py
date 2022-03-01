from traceback import print_tb
from unicodedata import name
from item import Item
from list import List
import requests
import dotenv
import os
import json

dotenv.load_dotenv()

api_url = os.getenv('TRELLO_URL')
api_key = os.getenv('TRELLO_API_KEY')
api_token = os.getenv('TRELLO_API_TOKEN')
board_id = os.getenv('TRELLO_BOARD_ID')