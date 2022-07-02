import asyncio
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from blackbird import findUsername
import logging
import os

app = Flask(__name__, static_folder='templates/static')
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
CORS(app, resources={r"/*": {"origins": "*"}})
loop = asyncio.get_event_loop()
logging.getLogger('werkzeug').disabled = True


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search/username' ,methods=["POST"])
def searchUsername():
    content = request.get_json()
    username = content['username']
    results = loop.run_until_complete(findUsername(username))
    return jsonify(results)


app.run('0.0.0.0')