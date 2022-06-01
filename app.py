from flask import Flask, jsonify, request, session, render_template, redirect, url_for, flash
from flask_cors import CORS, cross_origin
import sqlite3
from db import *

connect()

app= Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.secret_key = 'mysecret123'


@app.route("/", methods=['GET'])
def home():
    if session.get('user'):
        return render_template('home.html', times=get_times())
    return redirect(url_for('login'))

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        if check_user_psw(username, password):
            session['user'] = username
            return redirect(url_for('home'))
        else:
            return render_template('message.html', message="Wrong username or password", forward="login")
    return render_template('login.html')

@app.route("/logout", methods=['GET'])
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

#   --- API ENDPOINTS ---

@app.route("/times", methods=["GET"])
@cross_origin()
def message():
    output = ""
    for time in get_times():
        output += time + "|"
    return jsonify(output)
    

if __name__=='__main__':
    app.run(debug=True)