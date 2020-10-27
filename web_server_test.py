#!/usr/bin/env python

import os.path
from flask import Flask, jsonify, make_response, request, render_template, send_from_directory
from datetime import datetime

app = Flask(__name__, static_url_path='')

# API document
@app.route('/api/dout', methods=['GET'])
def apiDOut() :
    return jsonify({})

# API switchAvailable
@app.route('/api/available', methods=['GET'])
def apiavailable() :
    return jsonify({})

# API Busy
@app.route('/api/busy', methods=['GET'])
def apiBusy() :
    return jsonify({})

# API Away
@app.route('/api/away', methods=['GET'])
def apiAway() :
    return jsonify({})

# API switchMeeting
@app.route('/api/meeting', methods=['GET'])
def apiMeeting() :
    return jsonify({})

# API switchPhone
@app.route('/api/phone', methods=['GET'])
def apiPhone() :
    return jsonify({})

# API switchEmail
@app.route('/api/email', methods=['GET'])
def apiEmail() :
    return jsonify({})

# API switchVideo
@app.route('/api/video', methods=['GET'])
def apiVideo() :
    return jsonify({})

# API clear
@app.route('/api/clear', methods=['GET'])
def apiClear() :
    return jsonify({})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def index():
    return render_template('lcd.html')

@app.route('/js/<path:filename>')
def send_js(filename):
    return send_from_directory('js', filename)

@app.route('/css/<path:filename>')
def send_css(filename):
    return send_from_directory('css', filename)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
