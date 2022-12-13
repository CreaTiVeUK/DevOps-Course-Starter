import os

class Config:
    def __init__(self):
        """Base configuration variables."""
        self.MONGO_CON_STRING= os.environ.get('MONGO_CON_STRING')
        self.MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME')
        self.GITHUB_CLIENT_ID=os.environ.get('GITHUB_CLIENT_ID')
        self.GITHUB_CLIENT_SECRET=os.environ.get('GITHUB_CLIENT_SECRET')
        self.SECRET_KEY=os.environ.get('SECRET_KEY')
        self.LOGIN_DISABLED=os.environ.get('LOGIN_DISABLED') == 'True'
        
        ENV_VARIABLES = {
            'MONGO_CON_STRING':self.MONGO_CON_STRING,
            'MONGO_DB_NAME':self.MONGO_DB_NAME,
            'GITHUB_CLIENT_ID':self.GITHUB_CLIENT_ID,
            'GITHUB_CLIENT_SECRET':self.GITHUB_CLIENT_SECRET,
            'SECRET_KEY':self.SECRET_KEY,
            'LOGIN_DISABLED':self.LOGIN_DISABLED
            }
        
        for i in ENV_VARIABLES:
            if ENV_VARIABLES[i] == None:
                raise ValueError("No "+i+" set for Flask application. Did you follow the setup instructions?")
