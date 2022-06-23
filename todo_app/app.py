from flask import Flask, render_template, request, url_for, redirect
from todo_app.data.configs.flask_config import Config
from todo_app.data.ViewModel import ViewModel
import todo_app.data.session_items_trello as session
import todo_app.data.configs.logger_settings as logger

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    
    @app.route('/')
    def index():
        items = session.get_Items_and_Status()
        item_view_model = ViewModel(items) 
        return render_template('index.html', view_model=item_view_model)


    @app.route('/add_item', methods=['POST'])
    def add_item():
        title = request.form['filmTitle']
        logger.log.info('Title to add: ' + title)
        session.create_Card('To Do', title)
        return redirect(url_for('index'))


    @app.route('/item_description/<string:titleID>', methods=['GET', 'POST'])
    def item_description(titleID):
        description = request.form['description']
        logger.log.info('Card ID\'s description to update: ' + titleID)
        logger.log.info('Description: ' + description)
        session.update_item_description(titleID, description)
        return redirect(url_for('index'))


    @app.route('/item_due/<string:titleID>', methods=['GET', 'POST'])
    def item_due(titleID):
        due = request.form['date']
        logger.log.info('Card ID\'s : ' + titleID)
        logger.log.info('Card due date: ' + due)
        session.update_item_due_date(titleID, due)
        return redirect(url_for('index'))


    @app.route('/complete_item/<string:titleID>', methods=['POST'])
    def complete_item(titleID):
        logger.log.info('Attempting to move card to Done list: '+ titleID)
        session.move_Card('Done', titleID)
        return redirect(url_for('index'))


    @app.route('/doing_item/<string:titleID>', methods=['POST'])
    def doing_item(titleID):
        logger.log.info('Attempting to move card to Doing list: '+ titleID)
        session.move_Card('Doing', titleID)
        return redirect(url_for('index'))


    @app.route('/revert_item/<string:titleID>', methods=['POST'])
    def revert_item(titleID):
        logger.log.info('Attempting to move card to To Do list: '+ titleID)
        session.move_Card('To Do', titleID)
        return redirect(url_for('index'))
    
    return app

