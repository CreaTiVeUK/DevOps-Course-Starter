import os

class Config:
    def __init__(self):
        """Base configuration variables."""
        self.TRELLO_API_KEY = os.environ.get('TRELLO_API_KEY')
        self.TRELLO_API_TOKEN = os.environ.get('TRELLO_API_TOKEN')
        self.TRELLO_URL = os.environ.get('TRELLO_URL')
        self.TRELLO_BOARD_ID = os.environ.get('TRELLO_BOARD_ID')
        
        ENV_VARIABLES = {
            self.TRELLO_API_KEY,
            self.TRELLO_API_TOKEN,
            self.TRELLO_URL,
            self.TRELLO_BOARD_ID
            }
        
        for i in ENV_VARIABLES:
            if not i:
                raise ValueError("No "+i+" set for Flask application. Did you follow the setup instructions?")
