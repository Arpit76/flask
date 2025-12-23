from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)




class Note(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    title=  db.Column  (db.String,unique=True,nullable=False) 
    description= db.Column  (db.String)

with app.app_context():
    db.create_all()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/notes")
def getAllNotes():
    notes = db.session.execute(db.select(Note).order_by(Note.title)).all()
    #return render_template("user/list.html", users=users)
    myNotes=[]
    for note in notes:
        myNotes.append({"title": note[0].title,"description": note[0].description})
    return jsonify(myNotes)

@app.route("/create", methods=["GET", "POST"])
def note_create():
    if request.method == "POST":
        note = Note(
            title=request.form["title"],
            description=request.form["description"],
        )
        db.session.add(note)
        db.session.commit()
        return jsonify({"success1": True})
        

    #return render_template("user/create.html")

app.run(debug=True)
#app.run (host:"0.0.0.0","port":5000)