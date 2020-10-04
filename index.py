from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

softwareOn = False;

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/radio')
def playRadio():
	print("radio is now playing");
	return '', 200;

@app.route('/spotify')
def playSpotify():

	return render_template('index.html')

@app.route('/software-mode')
def controlBySoftware():
	softwareOn = True
	return '', 200;

@app.route('/volume', methods=['POST', 'GET'])
def controlVolume():
	if request.method == 'POST':
		volume = request.form['myRange']
		if(softwareOn):
			#logic
			# print(volume)
			print('yay')
	elif request.method == 'GET':
		print('get')
	return '', 200;

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
