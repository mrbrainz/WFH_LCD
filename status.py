#!/usr/bin/env python

import i2c_lcd_driver
import os.path
from time import sleep
from flask import Flask, jsonify, make_response, request, render_template, send_from_directory
from datetime import datetime
mylcd = i2c_lcd_driver.lcd()

app = Flask(__name__, static_url_path='')

def currentTime():
    dateraw=datetime.now()
    timeFormat=dateraw.strftime("%-I:%M %p")
    return timeFormat

def switchDOut() :
    mylcd.lcd_clear()
    mylcd.lcd_display_string("DO NOT ENTER", 1)
    mylcd.lcd_display_string("DICK LIKELY OUT", 2)
    sleep(1)

def switchAvailable() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Status:Available", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)

def switchBusy() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Status: Busy", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)

def switchAway() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Status: Away", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)

def switchMeeting() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("In a meeting", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)

def switchPhone() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("On the phone", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)

def switchEmail() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Sending Emails", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)

def switchVideo() :
    cT=currentTime()
    mylcd.lcd_clear()
    mylcd.lcd_display_string("On a video call", 1)
    mylcd.lcd_display_string("as of "+cT, 2)
    sleep(1)



def switchClear() :
    mylcd.lcd_clear()
    sleep(1)

# API document
@app.route('/api/dout', methods=['GET'])
def apiDOut() :
    switchDOut()
    return jsonify({})

# API switchAvailable
@app.route('/api/available', methods=['GET'])
def apiavailable() :
    switchAvailable()
    return jsonify({})

# API Busy
@app.route('/api/busy', methods=['GET'])
def apiBusy() :
    switchBusy()
    return jsonify({})

# API Away
@app.route('/api/away', methods=['GET'])
def apiAway() :
    switchAway()
    return jsonify({})

# API switchMeeting
@app.route('/api/meeting', methods=['GET'])
def apiMeeting() :
    switchMeeting()
    return jsonify({})

# API switchPhone
@app.route('/api/phone', methods=['GET'])
def apiPhone() :
    global globalLastCalledApi
    globalLastCalledApi = '/api/Phone'
    switchPhone()
    return jsonify({})

# API switchEmail
@app.route('/api/email', methods=['GET'])
def apiEmail() :
    switchEmail()
    return jsonify({})

# API switchVideo
@app.route('/api/video', methods=['GET'])
def apiVideo() :
    switchVideo()
    return jsonify({})

# API clear
@app.route('/api/clear', methods=['GET'])
def apiClear() :
    switchClear()
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
