from flask import Flask, render_template
import subprocess
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')
@app.route('/process_data/', methods=['POST'])
def script():
	#return "Hello"    	
	subprocess.run("sh ./script.sh", shell = True)

if __name__ == "__main__":
	app.run()
