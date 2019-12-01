import os

import subprocess
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def main():
	#print(os.environ)
	return render_template('index.html')


@app.route("/test/", methods=['POST'])
def test():
	a = request.form["a"]
	b = request.form["b"]
	return render_template('test.html', a = a, b = b)


@app.route('/process_data/', methods=['POST'])
def script():
	createVMreturn = subprocess.call("sh ./process_data.sh", shell = True)
	return str(createVMreturn)


if __name__ == "__main__":
	app.run()
	
