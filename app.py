from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/new-todo')
def new_todo():
    return "<li><input type='checkbox'> new todo</li>"

if __name__ == '__main__':
    app.run(debug=True)
