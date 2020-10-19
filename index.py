from flask import Flask, request, render_template, jsonify
import RPi.GPIO as GPIO
import serial
from os import system
from serial1 import read_serial
from buttons import read_pin
from volume_control import volume_control
import time
from spotify import spotify_off_software, spotify_on_software
#from radios import radio_on, radio_off
from radios import radio_on_software, radio_off_software
from usb import play_usb_software
import multiprocessing
global player
app = Flask(__name__)

NAMES = (
    "Radio 1 Rock",
    "Z-Rock",
)
STREAMS = (
    "http://149.13.0.81/radio1rock.ogg",
    "http://46.10.150.243:80/z-rock.mp3",
)

softwareOn = 0
playing = 0
current_volume = 500

radio_i = 0
spotify_i = 0
usb_i = 0


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/radio', methods = ['POST', 'GET'])
def playRadio():
	if request.method == 'POST':
		#radio = request.form['radio']
		global radio_i
		global player_radio
		if softwareOn:
			if(not(radio_i)):
				radio_i = 1 - radio_i
				print("radio started")
				player_radio=radio_on_software()
				player=player_radio
				
			else:
				radio_i = 1 - radio_i
				print("radio stopped")
				#p1 = multiprocessing.Process(target=radio_on, args=(STREAMS[NAMES.index('Z-Rock')],))
				#p1.start()
				radio_off_software(player_radio)
		return jsonify({'softwareOn' : softwareOn})
	#return '', 200;

@app.route('/spotify', methods = ['POST', 'GET'])
def playSpotify():
	if request.method == 'POST':
		
		global spotify_i
		if softwareOn:
			if spotify_i:
				spotify_i = 1 - spotify_i
				print("spotify stopped")
				spotify_off_software()
			else:
				spotify_i = 1 - spotify_i
				print("spotify is now playing")
				spotify_on_software()
		return jsonify({'softwareOn' : softwareOn})
	#return '', 200;

@app.route('/usb', methods  =['POST', 'GET'])
def playUSB():
	if request.method == 'POST':
		#usb = request.form['usb']
		global usb_i
		global player_usb
		print(usb_i)
		if(softwareOn):
			if(not(usb_i)):
				usb_i = 1 - usb_i
				player_usb=play_usb_software('/media/pi/flash/Deutschland.flac')
				#system('killall omxplayer.bin')
				#p2.kill()
				print("usb on")
			else:
				usb_i = 1 - usb_i
				#p2 = multiprocessing.Process(target=play_usb, args=())
				#p2.start()
				player_usb.quit()
				print("usb off")

		return jsonify({'softwareOn' : softwareOn})
	#return '', 200;

@app.route('/mode', methods = ['POST', 'GET'])
def controlBySoftware():
	if request.method == 'POST':
		global softwareOn
		state = request.form['toggleBar']
		if state == "true":
			softwareOn = 1
			print("softwareOn")
		elif state == "false":
			softwareOn = 0
			print("softwareOff")
	return '', 200;

@app.route('/volume', methods = ['POST', 'GET'])
def controlVolume():
	if request.method == 'POST':
		volume = request.form['myRange']
		if(int(volume)<520):
			volume=0
		global current_volume
		current_volume = volume
		step = 10
		value = float(volume)/step 

		if softwareOn:
			system("amixer sset 'Headphone' " + str(value) + '%')
			print('volume changed to ' + str(value))
		return jsonify({'softwareOn' : softwareOn})
	

@app.route('/play', methods = ['POST', 'GET'])
def controlStartStop():
	if request.method == 'POST':
		#state = request.form['play']
		global playing
		if softwareOn:
			if playing:
				print("if" + str(current_volume))
				# if radio_i:
				# 	value = 0
				# 	system('''export DBUS_SESSION_BUS_ADDRESS=$(cat /tmp/omxplayerdbus.${USER:-root})
				# 		dbus-send --print-reply --session --reply-timeout=500 --dest=org.mpris.MediaPlayer2.omxplayer /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Set string:"org.mpris.MediaPlayer2.Player" string:"Volume" double:''' + str(value))
				# if spotify_i:
				# 	system("amixer sset 'Headphone' " + str(0) + '%')
				system("amixer sset 'Headphone' " + str(0) + '%')
				playing = 1 - playing
			else:
				print("else" + str(current_volume))
				value = float(int(current_volume)/10)
				# 	system('''export DBUS_SESSION_BUS_ADDRESS=$(cat /tmp/omxplayerdbus.${USER:-root})
				# 		dbus-send --print-reply --session --reply-timeout=500 --dest=org.mpris.MediaPlayer2.omxplayer /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Set string:"org.mpris.MediaPlayer2.Player" string:"Volume" double:''' + str(value))
				# if spotify_i:
				system("amixer sset 'Headphone' " + str(value) + '%')
				playing = 1 - playing
			print('state changed to ' + str(playing))
		return jsonify({'softwareOn' : softwareOn})
	

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
