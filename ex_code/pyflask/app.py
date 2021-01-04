from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.raute('/info')
def info():
    return 'Info'
