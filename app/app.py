from initdb import db,app,User
from flask import render_template

@app.route("/")
def find_all_users():
    users = User.query.all()
    print(users)
    return render_template("list.html", users=users)


if __name__ == '__main__':
    app.run()

