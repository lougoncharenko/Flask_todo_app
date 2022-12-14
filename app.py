from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# This client variable contains a connection to your MongoDB database which should be running on port 27017.
client = MongoClient('localhost', 27017)

db = client.flask_db
todos = db.todos


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        priority = request.form['priority']
        todos.insert_one({'content': content, 'priority': priority})
        return redirect(url_for('index'))
    all_todos = todos.find()
    all_todos.collation({'locale': 'en'})
    all_todos.sort('priority')
    return render_template('index.html', todos=all_todos)

@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port = 3000)