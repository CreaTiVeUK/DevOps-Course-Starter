from flask import Flask, render_template, request, url_for, redirect
from todo_app.data.configs.flask_config import Config
from todo_app.data.view_model import ViewModel
from todo_app.data.mongo_db_client import MongoDBClient
import todo_app.data.configs.logger_settings as logger

def create_app():
    config = Config()
    app = Flask(__name__)
    app.config.from_object(config)
    mongo_db = MongoDBClient()
    

    @app.route('/')
    def index():
        items = mongo_db.get_items()
        item_view_model = ViewModel(items) 
        return render_template('index.html', view_model=item_view_model)


    @app.route('/add_item', methods=['POST'])
    def add_item():
        title = request.form['filmTitle']
        logger.log.info('Title to add: ' + title)
        mongo_db.add_item(title)
        return redirect(url_for('index'))


    @app.route('/item_description/<string:titleID>', methods=['GET', 'POST'])
    def item_description(titleID):
        description = request.form['description']
        logger.log.info('Card ID\'s description to update: ' + titleID)
        logger.log.info('Description: ' + description)
        mongo_db.update_document(titleID, 'description', description)
        return redirect(url_for('index'))


    @app.route('/item_due/<string:titleID>', methods=['GET', 'POST'])
    def item_due(titleID):
        due = request.form['date']
        logger.log.info('Card ID\'s : ' + titleID)
        logger.log.info('Card due date: ' + due)
        mongo_db.update_document(titleID, 'due', due)
        return redirect(url_for('index'))


    @app.route('/complete_item/<string:titleID>', methods=['POST'])
    def complete_item(titleID):
        logger.log.info('Attempting to move card to Done list: '+ titleID)
        mongo_db.update_document(titleID, 'status', 'Done')
        return redirect(url_for('index'))


    @app.route('/doing_item/<string:titleID>', methods=['POST'])
    def doing_item(titleID):
        logger.log.info('Attempting to move card to Doing list: '+ titleID)
        mongo_db.update_document(titleID, 'status', 'Doing')
        return redirect(url_for('index'))


    @app.route('/revert_item/<string:titleID>', methods=['POST'])
    def revert_item(titleID):
        logger.log.info('Attempting to move card to To Do list: '+ titleID)
        mongo_db.update_document(titleID, 'status', 'To Do')
        return redirect(url_for('index'))
    
    return app

