from asyncio import tasks
from re import U
from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route("/add-data", methods=["POST"])
def add_task() :
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)
app.run()