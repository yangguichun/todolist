from todolist import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    createTime = db.Column(db.DateTime)
    title = db.Column(db.Text)
    editTime = db.Column(db.Integer, default=0)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

# @db.event.listens_for(Todo.title, 'set')
# def increment_edit_time(target, value, oldValue, initiator):
#     if target.editTime is not None:
#         target.editTime += 1
