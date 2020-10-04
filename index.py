from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

softwareOn = 0;

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/radio', methods = ['POST', 'GET'])
def playRadio():
	print("radio is now playing");
	return '', 200;

@app.route('/spotify', methods  =['POST', 'GET'])
def playSpotify():

	return render_template('index.html')

@app.route('/mode', methods = ['POST', 'GET'])
def controlBySoftware():
	if request.method == 'POST':
		global softwareOn;
		state = request.form['toggleBar']
		if(state == "true"):
			softwareOn = 1
		elif(state == "false"):
			softwareOn = 0
		print(softwareOn)
		print(state)
	return '', 200;

@app.route('/volume', methods = ['POST', 'GET'])
def controlVolume():
	if request.method == 'POST':
		volume = request.form['myRange']
		# print("ti i si ma " + str(softwareOn))
		if(softwareOn):
			#logic
			print('yay')
		else:
			return jsonify({'softwareOn' : softwareOn})
		return jsonify({'softwareOn' : softwareOn})
	# elif request.method == 'GET':
	# 	print('get')
	return '', 200;

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
