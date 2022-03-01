from flask import Flask, render_template, request, url_for, redirect
from todo_app.flask_config import Config
from todo_app.data.item import Item
import todo_app.data.session_items_trello as session
import todo_app.logger_settings as logger

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html', cards=session.get_Items_and_Status()[0])


@app.route('/add_item', methods=['POST'])
def add_item():
    title = request.form['filmTitle']
    logger.log.info('Title to add: ' + title)
    Item.create_Card('To Do', title)
    return redirect(url_for('index'))


@app.route('/complete_item/<string:titleID>', methods=['GET'])
def complete_item(titleID):
    logger.log.info('Attempting to move card')
    logger.log.info('Item to move from To Do to Done: ' + titleID)
    Item.move_Card('Done', titleID)
    return redirect(url_for('index'))


@app.route('/revert_item/<string:titleID>', methods=['GET'])
def revert_item(titleID):
    logger.log.info('Attempting to move card')
    logger.log.info('Item to revert from Done to To Do: ' + titleID)
    Item.move_Card('To Do', titleID)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
