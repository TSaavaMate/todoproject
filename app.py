from flask import Flask, render_template, request, redirect, url_for
import time
from models import db, Todo

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/main")
def main():
    todo_list = Todo.query.all()
    return render_template("index.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    if not title:
        return redirect(url_for("main"))
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("main"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    time.sleep(1)
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("main"))


@app.route("/edit/<int:todo_id>")
def edit(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    return render_template("edit.html", item=todo)


@app.route("/save/<int:todo_id>", methods=["POST"])
def save(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    new_title = request.form.get("title")
    if not new_title:
        print("not new title")
    else:
        print("there is")

    if new_title == todo.title:
        return redirect(url_for("main"))

    todo.title = new_title
    db.session.commit()
    return redirect(url_for("main"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    time.sleep(2)
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("main"))


if __name__ == "__main__":
    app.run(debug=True)

if __name__ == '__main__':
    app.run()
