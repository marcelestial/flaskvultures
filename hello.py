from models import *
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
	vultures = Vulture.select().order_by(Vulture.speciesName.asc())
	return render_template('home.html', vultures=vultures)

@app.route("/best")
def best():
	return render_template('best.html')

if __name__ == "__main__":
	app.run(debug=True)
