from app import create_app
from flask_pymongo import PyMongo
from flask import Flask
app = create_app()
mongodb_client = PyMongo(app, uri="mongodb+srv://new:abcd1234@cluster0.sm1gh.mongodb.net/newd?retryWrites=true&w=majority")
db = mongodb_client.db


@app.route("/add_one")
def add_one():
    user = mongodb_client.db.job
    user.insert_one({'title': "todo title", 'body': "todo body"})
    return "ok"

if __name__ == '__main__': 
    app.run(debug=True)
    