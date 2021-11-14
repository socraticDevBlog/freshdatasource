from flask import Flask, json, jsonify, request


messages = [{"id": 1, "name": "message 1"}, {"id": 2, "name": "message 2"}]

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


# curl --header "Content-Type: application/json" --request POST http://localhost:5000/message --data "{\"name\":\"message 3\"}"
@app.route("/message", methods=["POST"])
def post_message():
    request_message = request.json

    new_id = max([message["id"] for message in messages]) + 1

    new_message = {"id": new_id, "name": request_message["name"]}

    messages.append(new_message)

    return jsonify(new_message), 201


# curl --header "Content-Type: application/json" --request PUT http://localhost:5000/message/3 --data "{\"name\":\"UPDATE message 3\"}"
@app.route("/message/<int:id>", methods=["PUT"])
def modify_message(id):
    updated_message = request.json

    for message in messages:
        if message["id"] == id:
            message["name"] = updated_message["name"]
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
