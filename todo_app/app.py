from flask import Flask
from flask import render_template

from todo_app.flask_config import Config
import todo_app.data.session_items as session

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html', items = session.get_items())

if __name__ == '__main__':
    app.run()
