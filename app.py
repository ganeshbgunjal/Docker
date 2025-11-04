# Flask app for Hello World example.
from flask import Flask
import os

app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello_world():
    return '<h1>Hello Ganesh, Welcome to the Docker World!</h1>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
