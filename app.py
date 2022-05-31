from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app= Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/times", methods=["GET"])
@cross_origin()
def message():
    #return jsonify("July 1st : 12:00 am (EST)   9:00 am (PST)|July 2nd : 12:00 am (EST)   9:00 am (PST)|July 3rd : 12:00 am (EST)   9:00 am (PST)|July 4th : 12:00 am (EST)   9:00 am (PST)")
    return jsonify("Carline is the sweetest!")

if __name__=='__main__':
    app.run(debug=True)