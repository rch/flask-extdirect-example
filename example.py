from flask import Flask, redirect, url_for, session, request
from flask.ext.sencha import direct
from example_utils import RedisSessionInterface

app = Flask(__name__)
app.config['SESSION_COOKIE_NAME'] = 'example'
app.session_interface = RedisSessionInterface()
app.register_blueprint(direct.blueprint, url_prefix='/direct')

@app.route("/")
def index():
    return redirect(url_for('static', filename='index.html'))

@app.route("/clear")
def clear():
    session.clear()
    return redirect(url_for('static', filename='index.html'))

@app.route("/chk")
def check():
    print request.headers
    print request.cookies
    print app.config
    return 'OK'

app.secret_key = '\xf4\xf70Q\x90\xe7k\xbe=\x1b\x8f\xee\xb8zFh\x0c\xdd\x18x\x12;N{' 

if __name__ == "__main__":
    app.run(debug=True)
