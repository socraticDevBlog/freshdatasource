from flask import Flask, json, jsonify, request
from database import Database
from logger import Logger
from utils import tupleToString


# trigger DEBUG logging mode by adding integer param 10 in Terminal
# this way :  $python job_scraper.py 10
#
logger_verbosity_level = Logger.LOWEST_VERBOSITY
logger = Logger(__name__, logger_verbosity_level)


try:    
    db = Database()
    # uncomment on first execution : will create a database file and a table
    # db.create_database()
    # OTHERWISE : ALWAYS KEEP THIS LINE COMMENTED
except Exception as ex:
    logger.error('unable to create database object : ' + tupleToString(ex.args))


messages = [{"id": 1, "text": "message 1"}, {"id": 2, "text": "message 2"}]

app = Flask(__name__)

# curl -v http://localhost:5000/messages
@app.route("/messages")
def get_messages():
    return jsonify(messages)


# curl -v http://localhost:5000/message/1
@app.route("/message/<int:id>")
def get_message(id):
    list = [message for message in messages if message["id"] == id]
    if len(list) == 0:
        return f"message with id {id} not found", 404
    return jsonify(list[0])


# curl --header "Content-Type: application/json" --request POST http://localhost:5000/message --data "{\"text\":\"message 3\"}"
@app.route("/message", methods=["POST"])
def post_message():
    request_message = request.json

    new_id = max([message["id"] for message in messages]) + 1

    new_message = {"id": new_id, "text": request_message["text"]}

    messages.append(new_message)

    return jsonify(new_message), 201


# curl --header "Content-Type: application/json" --request PUT http://localhost:5000/message/3 --data "{\"text\":\"UPDATE message 3\"}"
@app.route("/message/<int:id>", methods=["PUT"])
def modify_message(id):
    updated_message = request.json

    for message in messages:
        if message["id"] == id:
            message["text"] = updated_message["text"]
            return jsonify(message), 200

    return f"message with id {id} was not found", 404


# curl -v http://localhost:5000/message/2 --request DELETE
@app.route("/message/<int:id>", methods=["DELETE"])
def delete_message(id):
    messages_list = [message for message in messages if message["id"] == id]

    if len(messages_list) == 1:
        messages.remove(messages_list[0])
        return f"message with id {id} deleted", 200

    return f"message with id {id} nof found", 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
