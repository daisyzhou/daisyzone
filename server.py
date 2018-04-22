from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from madlibs import library

from collections import defaultdict

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route('/radlibs')
def madlibs_home():
    # TODO home should show a list or or something
    name = library.get_random_name()
    return redirect("/radlibs/{}".format(name))


@app.route('/radlibs/<template_name>')
def madlib(template_name):
    template = library.get_by_name(template_name)
    print("debug: modifications: {}".format(template.get_modifications()))
    return render_template("madlibs.html", modifications=template.get_modifications(), template_name=template_name)


@app.route('/radlibs/<template_name>/answer', methods=['POST'])
def madlib_answer(template_name):
    answers = []
    print("hi")
    template = library.get_by_name(template_name)
    description_occurences = defaultdict(lambda: 0)
    for _, description in template.get_modifications():
        answers.append(request.form.getlist(description)[description_occurences[description]])
        description_occurences[description] += 1

    filled_in_madlib = library.get_by_name(template_name).fill_in_answers(answers)
    return render_template("madlibs_answer.html", filled_in_madlib=filled_in_madlib)
