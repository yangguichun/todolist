from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('todolist')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:00@127.0.0.1/todolist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from todolist import commands, views
