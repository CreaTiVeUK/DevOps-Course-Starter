from flask import Flask, render_template
from flask.globals import request
from flask.wrappers import Request
from todo_app.flask_config import Config
import todo_app.data.session_items as session

#Trello API key -> 6a36bc3254f4441f08c8207b0da716fa
#Trello token -> f16c623ce612b724f1ca17ab93f0c2bc7373cc5f70416e856e7ec57ee1779b73
#Trello board -> https://trello.com/b/RZcQuIck/to-do -> RZcQuIck
#Thunder client

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html', items = session.get_items())


@app.route('/add_item', methods=['POST'])  
def add_item():
    title = request.form['filmTitle']
    session.add_item(title)
    return index()


if __name__ == '__main__':
    app.run()
