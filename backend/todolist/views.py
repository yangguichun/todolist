from todolist import app, db
from todolist.models import Todo
from flask import jsonify
from datetime import datetime


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
