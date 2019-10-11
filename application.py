from flask import Flask,render_template
import datetime

app = Flask(__name__)

@app.route("/home")
def index():
	headline  = "hello "
	names = ["dafs","dsfsa","dsafsdf"]
	return render_template("index.html",headline = headline,names = names)

@app.route("/<string:name>")
def hello(name):
	return "hello {name}"
    
if __name__ == "__main__":
    app.run(debug=True)