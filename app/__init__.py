from flask import Flask

# Initialize application
app = Flask(__name__)

@app.route('/')
def hello():
    return "Tweet a compliment sandwich to the biggest asshole of the modern age - coming soon"
