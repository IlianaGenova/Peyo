from flask import Flask, request, render_template, jsonify
from spotify import spotify_off, spotify_on
from volume_control import volume_control
from usb import play_usb

app = Flask(__name__)

softwareOn = 0;
playing = 0;

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/radio', methods = ['POST', 'GET'])
def playRadio():
	if request.method == 'POST':
		radio = request.form['radio']
		if(softwareOn):
			print("radio is now playing")
		return jsonify({'softwareOn' : softwareOn})
	return '', 200;

@app.route('/spotify', methods  =['POST', 'GET'])
def playSpotify():
	if request.method == 'POST':
		spotify = request.form['spotify']
		if(softwareOn):
			spotify_on()
			print("spotify is now playing")
		return jsonify({'softwareOn' : softwareOn})
	return '', 200;

@app.route('/usb', methods  =['POST', 'GET'])
def playUSB():
	if request.method == 'POST':
		usb = request.form['usb']
		if(softwareOn):
			play_usb()
			print("usb is now on")
		return jsonify({'softwareOn' : softwareOn})
	return '', 200;

@app.route('/mode', methods = ['POST', 'GET'])
def controlBySoftware():
	if request.method == 'POST':
		global softwareOn;
		state = request.form['toggleBar']
		if(state == "true"):
			softwareOn = 1
			print("softwareOn")
		elif(state == "false"):
			softwareOn = 0
			print("softwareOff")
	return '', 200;

@app.route('/volume', methods = ['POST', 'GET'])
def controlVolume():
	if request.method == 'POST':
		volume = request.form['myRange']
		if(softwareOn):
			radio_on(STREAM)
			print('volume changed to ' + volume)
		return jsonify({'softwareOn' : softwareOn})
	return '', 200;

@app.route('/play', methods = ['POST', 'GET'])
def controlStartStop():
	if request.method == 'POST':
		state = request.form['play']
		if(softwareOn):
			global playing;
			playing = 1 - playing;
			print('state changed to ' + str(playing))
		return jsonify({'softwareOn' : softwareOn})
	return '', 200;

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
