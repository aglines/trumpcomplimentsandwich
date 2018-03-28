from flask import Flask, render_template
from random import randint

# Initialize application
app = Flask(__name__)

@app.route('/')
def hello():
    tweetText = assembleText()
    tweetURL = assembleURL(tweetText)
    return render_template('index.html', tweetText=tweetText, tweetURL=tweetURL)



def assembleText():
    randIntro = randint(0,19)
    randMid = randint(0,29)
    randOutro = randint(0,19)

# changing these to ascii hex codes for urlToTweet
#   %20 for space
#   %21 for exclamation point
#   %27 for single quote
#   %2E for period
    listIntro = [
    'MAGA%20TRUMP%21',
    'TRUMP%202020%21',
    'TRUMP%20America%20Great%21',
    'Keep%20America%20TRUMP%21',
    'TRUMP%20steaks%20great%21',
    'TRUMP%20Tower%20lu$$xury%21',
    'TRUMP%20#1%21',
    'So%20great%20TRUMP%21',
    'Handsomest%20Prez%20TRUMP%21',
    'TRUMP%20$$$%21',
    '$$%20TRUMP%20so%20rich%21',
    'TRUMP%20the%20BEST%21',
    'TRUMP%20strong%20POWER%21',
    'TRUMPs%20handsome%20genes%21',
    'Clear%20WINNER%21',
    'TRUMP%20knows%21',
    'World%27s%2E%20Best%2E%20TRUMP%21',
    'My%20hero%20TRUMP%21',
    'Rename%20it%20TRUMPDAY%21',
    'Winning%20TRUMP%21']

    listMid = [
    'jail%20time%20for%20you.',
    'you%27re gonna die in prison.',
    'your father never loved you.',
    'your dad never cared about you.',
    'DC lawyers all know you%27re poison.',
    'you can%27t trust your men anymore.',
    'impeached before long.',
    'no lawyer is dumb enough to defend you now.',
    'everyone knows you%27re poor.',
    'you feel old and you look old.',
    'we can all see you%27re horribly bald.',
    'walls are closing in.',
    'lawyers are too smart for you.',
    'lawyers can smell your lies.',
    'every old buddy is ratting on you this very moment.',
    'your sons only want your money.',
    'he only wants your money.',
    'white house staff fleeing this sinking ship.',
    'don jr dancing on your grave.',
    'ivanka and jared are ratting on you.',
    'lawyers are all jumping ship.',
    'hope hicks is ratting on you now too.',
    'ivanka talked to mueller can%27t trust her.',
    'don jr talk to mueller can%27t trust him.',
    'jared talked to mueller.',
    'can%27t trust them better fire them.',
    'can%27t even trust your bodyguards now.',
    'they%27re coming for you.',
    'they%27re going to get you in your sleep.',
    'don%27t trust your bodyguards.']

    listOutro = [
    'TRUMP family 4ever%21',
    'TRUMP give em hell%21',
    'TrUmP%21',
    'TRUMP Richest Prez%21',
    'TRUMP Best Potus ever%21',
    'Trump Power%21',
    'TRUMP Muscle%21',
    'TRUMP America%21',
    'TRUMP America GREAT%21',
    'TRUMP Tower GOLD$$%21',
    'TRUMP $$%21%21',
    '$$ TRUMP so rich%21',
    'TRUMP Tower $trong%21',
    'TRUMP America Great Again%21',
    'MAGA bitches%21%21',
    'MAGA 2024%21',
    'MAGA Biggest fans%21',
    'TRUMP MAGA biggest ever%21',
    'MAGA 2020%21',
    '2020 TRUMP%21'
    ]

    sandwich = '@realDonaldTrump%20' + listIntro[randIntro] + ' ' + listMid[randMid] + ' ' + listOutro[randOutro]

    return sandwich

def assembleURL(tweetText):
    urlToTweet='https://twitter.com/intent/tweet?original_referer=http%3A%2F%2Ftrumpcompliments.com%2F&ref_src=twsrc%5Etfw&text=' + tweetText + '&tw_p=tweetbutton&url=http%3A%2F%2Ftrumpcompliments.com'
    return urlToTweet
