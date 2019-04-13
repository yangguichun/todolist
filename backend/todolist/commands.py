from todolist import app, db
from todolist.models import Todo
import click
from datetime import datetime


@app.cli.command()
def createtable():
    db.create_all()
    click.echo('table created')


@app.cli.command()
def droptable():
    db.drop_all()
    click.echo('table droped')


@app.cli.command()
@click.argument('id')
def updatetodo(id):
    todo = Todo.query.filter_by(id=id).first()
    todo.title = todo.title + '更新了'
    db.session.commit()


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
