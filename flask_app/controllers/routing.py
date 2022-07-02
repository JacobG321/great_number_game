
from flask_app import app
from flask import render_template, redirect, session, request
import random


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/YesOrNo', methods=['POST'])
def yes_or_no():
    #this will make it so the number does not change everytime
    if 'num' not in session:
        session['num'] = random.randint(1, 100)

    number = int(request.form['number'])
    #this could also be render_template in the return section
    if number == session['num']:
        return redirect('/correct.html')
    elif number > session['num']:
        return redirect('/toohigh.html')
    elif number < session['num']:
        return redirect('/toolow.html')

@app.route('/correct.html')
def correct():
    session.clear()
    return render_template("correct.html")

@app.route('/toohigh.html')
def toohigh():
    return render_template("toohigh.html")

@app.route('/toolow.html')
def toolow():
    return render_template("toolow.html")

