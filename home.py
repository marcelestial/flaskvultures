from models import *
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
	vultures = Vulture.select().order_by(Vulture.speciesId.asc())
	return render_template('home.html', vultures=vultures)

@app.route("/detail")
def detail():
	return render_template('detail.html')

if __name__ == "__main__":
	app.run(debug=True)
