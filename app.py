from flask import Flask ,render_template
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.config["SQALALCHEMY_DATABASE_URL"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLAlchemy(app)
@app.route("/")
def home():
    return render_template ('index.html')

@app.route("/projects")
def projects():
    return "this is my project page"

if __name__ == '__main__':
    app.run(debug=True)
