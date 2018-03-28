from flask import Flask, render_template
from random import randint

# Initialize application
app = Flask(__name__)

@app.route('/')
def hello():
    tweetText = assembleText()
    return render_template('index.html', tweetText=tweetText)

def assembleText():
    randIntro = randint(0,2)
    randMid = randint(0,2)
    randOutro = randint(0,1)

    listIntro = ['intro1', 'intro2', 'intro3']
    listMid = ['mid1', 'mid2', 'mid3']
    listOutro = ['out1', 'out2']

    sandwich = listIntro[randIntro] + ' ' + listMid[randMid] + ' ' + listOutro[randOutro]

    return sandwich
