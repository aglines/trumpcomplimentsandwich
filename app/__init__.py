from flask import Flask, render_template
from random import randint

# Initialize application
app = Flask(__name__)

@app.route('/')
def hello():
    tweetText = assembleText()
    return render_template('index.html', tweetText=tweetText)

def assembleText():
    randIntro = randint(0,19)
    randMid = randint(0,29)
    randOutro = randint(0,19)

    listIntro = [
    'MAGA TRUMP!',
    'TRUMP 2020!',
    'TRUMP America Great!',
    'Keep America TRUMP! ',
    'TRUMP steaks great! ',
    'TRUMP Tower lu$$xury!',
    'TRUMP #1 ',
    'So great TRUMP!',
    'Handsomest Prez ever TRUMP!',
    'TRUMP $$$!!',
    '$$ TRUMP so rich!! ',
    'TRUMP the BEST! HAHA',
    'TRUMP strongman POWER. ',
    'TRUMPs handsome genes!',
    'Clear WINNER!',
    'TRUMP knows #fakenews.',
    'World\'s. Best. TRUMP.',
    'My hero TRUMP!',
    'Rename it TRUMPDAY!',
    'Trump winning!']

    listMid = [
    'jail for you',
    'you\'re gonna die in prison',
    'your father never loved you',
    'your dad never cared about you',
    'DC lawyers all know you\'re poison',
    'you can\'t trust your men anymore',
    'impeached before long',
    'no lawyer is dumb enough to defend you now',
    'everyone knows you\'re poor',
    'you feel old and you look old',
    'we can all see you\'re horribly bald',
    'walls are closing in',
    'lawyers are too smart for you',
    'lawyers can smell your lies',
    'every old buddy is ratting on you this very moment',
    'your sons only want your money',
    'he only wants your money',
    'white house staff fleeing this sinking ship',
    'don jr dancing on your grave',
    'ivanka and jared are ratting on you',
    'lawyers are all jumping ship',
    'hope hicks is ratting on you now too',
    'ivanka talked to mueller can\'t trust her',
    'don jr talk to mueller can\'t trust him',
    'jared talked to mueller',
    'can\'t trust them better fire them',
    'can\'t even trust your bodyguards now',
    'they\'re coming for you',
    'they\'re going to get you in your sleep',
    'don\'t trust your bodyguards']

    listOutro = [
    'TRUMP family 4ever!',
    'Give em hell Donald!',
    'Go Trump!',
    'Richest Prez $TRUMP ever!',
    'Best Potus TRUMP ever!',
    'POWER Trump!',
    'TRUMP muscle!',
    'TRUMP America!',
    'Make TRUMP America GREAT!',
    'TRUMP tower GOLD$$!',
    'TRUMP $$!!',
    '$$ TRUMP so rich!',
    'TRUMP Tower Strong!',
    'TRUMP America Great Again!',
    'MAGA bitches!!',
    'MAGA 2024!',
    'Biggest TRUMP fans!',
    'TRUMP the biggest ever!',
    'MAGA 2020!!',
    '2020 TRUMP!!'
    ]

    sandwich = listIntro[randIntro] + ' ' + listMid[randMid] + ' ' + listOutro[randOutro]

    return sandwich
