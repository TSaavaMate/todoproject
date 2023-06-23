from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

    def __str__(self):
        return "{{id:" + self.id + "}" + "{title:" + self.title + "}" + "{complete:" + self.complete + "}}"

    __repr__ = __str__
