from flask import Flask, jsonify, request, session, render_template, redirect, url_for, flash
from flask_cors import CORS, cross_origin
import sqlite3
from db import *

connect()

app= Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.secret_key = 'mysecret123'


@app.route("/", methods=['GET', 'POST'])
def home():
    if not(session.get('user')):
        return render_template("message.html", message="Please log in first", forward="/login")
    
    return render_template('home.html')

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
            return render_template('message.html', message="Wrong username or password", forward="/login")
    return render_template('login.html')

@app.route("/logout", methods=['GET'])
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


@app.route("/users", methods=['GET', 'POST'])
def users():
    if not(session.get('user')):
        return render_template("message.html", message="Please log in first", forward="/login")
    
    if request.method == 'POST':
        pass

    return render_template("user_management.html")

@app.route("/classes", methods=['GET', 'POST'])
def classes():
    if not(session.get('user')):
        return render_template("message.html", message="Please log in first", forward="/login")
    
    if request.method == 'POST':
        id = request.form['id']
        input = request.form.get('input_' + id)
        update_time(id, input)
        print(f"id: {id}", f"input: {input}")

    return render_template('class_times.html', times=get_times())

@app.route("/jobs", methods=['GET', 'POST'])
def jobs():
    if not(session.get('user')):
        return render_template("message.html", message="Please log in first", forward="/login")
    
    if request.method == 'POST':
        pass

    return render_template("job_board.html")

#   --- API ENDPOINTS ---

@app.route("/times", methods=["GET"])
@cross_origin()
def message():
    times = get_times()
    output_list = []
    for time in times:
        output_list.append(time[1])
    output = ""
    for time in output_list:
        output += time + "|"
    return jsonify(output)
    

if __name__=='__main__':
    app.run(debug=True)