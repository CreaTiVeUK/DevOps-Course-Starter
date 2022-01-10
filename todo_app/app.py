from flask import Flask, render_template, redirect
from flask.globals import request
from todo_app.flask_config import Config
import todo_app.data.session_items as session


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html', items = session.get_items())


@app.route('/add_film', methods=['POST'])  
def add_film():
    title = request.form['filmTitle']
    session.add_film(title)
    return redirect("/", code=302)


if __name__ == '__main__':
    app.run()
