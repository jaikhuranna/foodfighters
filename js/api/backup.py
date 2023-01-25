
from flask import Flask, jsonify, request

app = Flask(__name__)

# A welcome message to test our server
@app.route('/')
def index():
    return "Welcome to our API!"
# GET request 
@app.route('/getmsg/', methods=['GET'])
def get_message():
    return jsonify({'message': 'This is a GET request'})

# POST request
@app.route('/postmsg/', methods=['POST'])
def post_message():
    message = request.get_json(force=True)
    ik = message["ingredients"]
    return jsonify({'message': ik, 'data': message})


if __name__ == '__main__':
    app.run()
    