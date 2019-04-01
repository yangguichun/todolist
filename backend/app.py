from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import click

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:00@127.0.0.1/todolist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    createTime = db.Column(db.DateTime)
    title = db.Column(db.Text)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


@app.cli.command()
def createtable():
    db.create_all()
    click.echo('table created')

@app.cli.command()
def inittodo():
    todos = [
        '我要去新疆',
        '我要去云南',
        '我要去贵州',
        '我要去四川',
        '我要去重庆',
    ]
    for item in todos:
        n1 = Todo(title=item, createTime= datetime.now())
        db.session.add(n1)
        db.session.commit()
    click.echo('init the todolist')

@app.cli.command()
def readtodo():
    todos = Todo.query.all()
    for todo in todos:
        click.echo(todo.to_json())
    click.echo('read all todo item')


@app.cli.command()
def cleartodo():
    # db.session.delete(Todo)
    # db.session.commit()
    # Todo.delete()
    todos = Todo.query.all()
    for todo in todos:
        db.session.delete(todo)
    db.session.commit()
    click.echo('clear todolist table')

@app.cli.command()
def hello():
    click.echo('hello human')


@app.route('/gettodolist')
def gettodolist():
    todos = Todo.query.all()
    result = []
    for todo in todos:
        result.append(todo.to_json())
    return jsonify(list=result)

@app.route('/del/<id>')
def deltodo(id):
    todo = Todo.query.filter_by(id=id).first()
    if todo != None:
        db.session.delete(todo)
        db.session.commit()
        return jsonify(msg='success')
    return jsonify(msg='fail')

@app.route('/add', methods=['POST'])
def addtodo():
    todo = Todo(createTime=datetime.now(), title=request.json['title'])
    db.session.add(todo)
    db.session.commit()
    return jsonify(id=todo.id)


if __name__ == '__main__':
    app.run()
