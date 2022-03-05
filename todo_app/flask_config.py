import os


class Config:
    """Base configuration variables."""
    ENV_VARIABLES = {
        "TRELLO_API_KEY": os.environ.get('TRELLO_API_KEY'),
        "TRELLO_API_TOKEN": os.environ.get('TRELLO_API_TOKEN'),
        "TRELLO_URL": os.environ.get('TRELLO_URL'),
        "TRELLO_BOARD_ID": os.environ.get('TRELLO_BOARD_ID')
        }
    for key, value in ENV_VARIABLES.items():
        if not value:
            raise ValueError("No "+key+" set for Flask application. Did you follow the setup instructions?")
