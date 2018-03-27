from flask import Flask

# Initialize application
app = Flask(__name__)

@app.route('/')
def hello():
    return "hedsfsllo world"
