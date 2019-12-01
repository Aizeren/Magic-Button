import os
import sys

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def main():
	return render_template('index.html')


@app.route('/process_data/', methods=['POST'])
def process_data():
	#create vars with values of fields
	a = request.form["a"]
	b = request.form["b"]
	#create virtual machine
	createVMreturn = os.system("ansible-playbook createVM.yml")
	doingWellReturn = os.system("ansible-playbook doing_well.yml --extra-vars \"a="+a+" b="+b+"\"")
	result_file = open("./results/test.txt", "r")
	res = result_file.read()
	result_file.close()
	return render_template('result.html', res = res)


if __name__ == "__main__":
	app.run(debug=True)
	
