from flask import Flask, render_template
from flask.globals import request
from todo_app.flask_config import Config
import todo_app.data.session_items_trello as session
import todo_app.logger_settings as Logger

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html', cards = session.get_Lists_and_Cards()[0])


@app.route('/add_item', methods=['POST'])  
def add_item():
    title = request.form['filmTitle']
    Logger.log.info('Title to add: ' + title)
    session.create_Card('To Do', title)
    return index()


if __name__ == '__main__':
    app.run()
