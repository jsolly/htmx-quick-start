from flask import Flask, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/new-todo')
def new_todo():
    return "<li><input type='checkbox'> new todo</li>"


@app.route('/lambda-todo')
def lambda_todo():
    response = requests.get("")
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
