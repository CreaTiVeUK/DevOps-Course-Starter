import os
import dotenv

dotenv.load_dotenv()

api_url = os.getenv('TRELLO_URL')
api_key = os.getenv('TRELLO_API_KEY')
api_token = os.getenv('TRELLO_API_TOKEN')
board_id = os.getenv('TRELLO_BOARD_ID')