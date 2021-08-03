from app import app, config
from flask import render_template, redirect, url_for, request

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/map')
def viewmap():
    return 'hello world'

@app.route('/donate')
def donate():
    return 'hello world'

@app.route('/volunteer')
def volunteer():
    return 'hello world'

@app.route('/businesses')
def businesses():
    return 'hello world'

@app.route('/gethelp')
def gethelp():
    return 'hello world'