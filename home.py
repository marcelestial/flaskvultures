from models import *
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
  vultures = Vulture.select().order_by(Vulture.speciesId.asc())
  return render_template('home.html', vultures=vultures)

@app.route("/detail")
def detail():
  speciesId = request.args.get('id') #snag 'id' argument from url
  speciesName = Vulture.get(Vulture.speciesId == speciesId).speciesName
  description = Vulture.get(Vulture.speciesId == speciesId).description
  return render_template('detail.html', speciesId=speciesId, speciesName=speciesName, description=description)

@app.route("/add")
def add():
  return render_template('add.html')

@app.route("/edit")
def edit():
  speciesId = request.args.get('id') #snag 'id' argument from url
  return render_template('edit.html', speciesId=speciesId)

if __name__ == "__main__":
	app.run(debug=True)
