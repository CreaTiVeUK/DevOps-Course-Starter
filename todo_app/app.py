from flask import Flask, render_template, request, url_for, redirect
import requests
from todo_app.data.configs.flask_config import Config
from todo_app.data.view_model import ViewModel
from todo_app.data.mongo_db_client import MongoDBClient
from todo_app.data.User import User
from flask_login import LoginManager, login_required, login_user, current_user
import todo_app.data.configs.logger_settings as logger
from functools import wraps

def create_app():
    config = Config()
    app = Flask(__name__)
    app.config.from_object(config)
    mongo_db = MongoDBClient()

    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthenticated():
        return redirect(f"https://github.com/login/oauth/authorize?client_id={app.config['GITHUB_CLIENT_ID']}")

    @login_manager.user_loader
    def load_user(user_id):
        return User(user_id)

    login_manager.init_app(app)
    
    @app.route('/login/callback')
    def callback():
        code = request.args.get('code')
        token_headers = {
            "Accept": 'application/json'
        }
        token_body = {
            "client_id": app.config['GITHUB_CLIENT_ID'],
            "client_secret": app.config['GITHUB_CLIENT_SECRET'],
            "code": code
        }
        url = f"https://github.com/login/oauth/access_token"
        response=requests.post(url, token_body, headers = token_headers)
        access_token = response.json()['access_token']
        auth_headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer " + access_token
        }
        auth_url = 'https://api.github.com/user'
        auth_response = requests.get(auth_url, headers = auth_headers)
        username = auth_response.json()['login']
        user = User(username)
        login_user(user)

        return redirect(url_for('index'))

    def requires_writer(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.role == 'writer':
                return f(*args, **kwargs)
            else:
                return redirect(url_for('index'))    
        return wrapped

    @app.route('/')
    @login_required
    def index():
        items = mongo_db.get_items()
        item_view_model = ViewModel(items) 
        return render_template('index.html', view_model=item_view_model)


    @app.route('/add_item', methods=['POST'])
    @login_required
    @requires_writer
    def add_item():
        title = request.form['filmTitle']
        logger.log.info('Title to add: ' + title)
        mongo_db.add_item(title)
        return redirect(url_for('index'))


    @app.route('/item_description/<string:titleID>', methods=['GET', 'POST'])
    @login_required
    @requires_writer
    def item_description(titleID):
        description = request.form['description']
        logger.log.info('Card ID\'s description to update: ' + titleID)
        logger.log.info('Description: ' + description)
        mongo_db.update_document(titleID, 'description', description)
        return redirect(url_for('index'))


    @app.route('/item_due/<string:titleID>', methods=['GET', 'POST'])
    @login_required
    @requires_writer
    def item_due(titleID):
        due = request.form['date']
        logger.log.info('Card ID\'s : ' + titleID)
        logger.log.info('Card due date: ' + due)
        mongo_db.update_document(titleID, 'due', due)
        return redirect(url_for('index'))


    @app.route('/complete_item/<string:titleID>', methods=['POST'])
    @login_required
    @requires_writer
    def complete_item(titleID):
        logger.log.info('Attempting to move card to Done list: '+ titleID)
        mongo_db.update_document(titleID, 'status', 'Done')
        return redirect(url_for('index'))


    @app.route('/doing_item/<string:titleID>', methods=['POST'])
    @login_required
    @requires_writer
    def doing_item(titleID):
        logger.log.info('Attempting to move card to Doing list: '+ titleID)
        mongo_db.update_document(titleID, 'status', 'Doing')
        return redirect(url_for('index'))


    @app.route('/revert_item/<string:titleID>', methods=['POST'])
    @login_required
    @requires_writer
    def revert_item(titleID):
        logger.log.info('Attempting to move card to To Do list: '+ titleID)
        mongo_db.update_document(titleID, 'status', 'To Do')
        return redirect(url_for('index'))
    
    return app

