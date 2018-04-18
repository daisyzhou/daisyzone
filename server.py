from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/radlibs')
def madlibs_home():
    return render_template("madlibs.html")

@app.route('/radlibs/answer', methods=['POST'])
def madlibs_answer():
    noun1 = request.form(["noun1"])
    return render_template("madlibs.html")
