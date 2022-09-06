import os

class Config:
    def __init__(self):
        """Base configuration variables."""
        self.MONGO_CON_STRING= os.environ.get('MONGO_CON_STRING')
        self.MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME')
        self.GITHUB_CLIENT_ID=os.environ.get('GITHUB_CLIENT_ID')
        self.GITHUB_CLIENT_SECRET=os.environ.get('GITHUB_CLIENT_SECRET')
        
        ENV_VARIABLES = {
            self.MONGO_CON_STRING,
            self.MONGO_DB_NAME,
            self.GITHUB_CLIENT_ID,
            self.GITHUB_CLIENT_SECRET
            }
        
        for i in ENV_VARIABLES:
            if not i:
                raise ValueError("No "+i+" set for Flask application. Did you follow the setup instructions?")
