from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# This client variable contains a connection to your MongoDB database which should be running on port 27017.
client = MongoClient('localhost', 27017)

db = client.flask_db
todos = db.todos