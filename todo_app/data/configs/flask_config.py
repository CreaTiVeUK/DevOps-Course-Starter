import os

class Config:
    def __init__(self):
        """Base configuration variables."""
        self.MONGO_CON_STRING= os.environ.get('MONGO_CON_STRING')
        self.MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME')
        
        ENV_VARIABLES = {
            self.MONGO_CON_STRING,
            self.MONGO_DB_NAME
            }
        
        for i in ENV_VARIABLES:
            if not i:
                raise ValueError("No "+i+" set for Flask application. Did you follow the setup instructions?")
