from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    #!/usr/bin/env python3

    print("Content-type: text/html")
    print()
    print("<h1>Hello world!</h1>")
    return "Hello my World!"
