from flask import Flask, render_template
from flask.globals import request
from flask.wrappers import Request
from todo_app.flask_config import Config
import todo_app.data.session_items_trello as session

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html', cards = session.get_Lists_and_Cards()[0])

@app.route('/add_item', methods=['POST'])  
def add_item():
    title = request.form['filmTitle']
    session.add_item(title)
    return index()


if __name__ == '__main__':
    app.run()
