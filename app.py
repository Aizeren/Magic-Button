from flask import Flask, render_template, request
import subprocess
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')
@app.route('/process_data/', methods=['POST'])
def script():
	if (subprocess.check_call("sh ./script.sh") == 1):
		return "tuta"
	else:
		return "lol loshara"
	a = request.form['a']
	b = request.form['b']
	return str(float(a)+float(b))

if __name__ == "__main__":
	app.run()
	
