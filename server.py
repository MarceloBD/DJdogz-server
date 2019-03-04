import os, sys
from flask import Flask, jsonify, request, redirect


app = Flask(__name__)

@app.route('/')
def display():
    return 'here'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
