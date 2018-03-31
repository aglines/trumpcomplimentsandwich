from flask import Flask, render_template
from random import randint
import re


# Initialize application
app = Flask(__name__)

@app.route('/')
def tweet():
    tweetIntro = assembleIntro()
    tweetMid = assembleMid()
    tweetOutro = assembleOutro()

    tweetText = '@realdonaldtrump ' + tweetIntro + ' ' + tweetMid + ' ' + tweetOutro

    tweetURL = assembleURL(tweetText)

    return render_template('index.html', tweetIntro=tweetIntro, tweetMid=tweetMid, tweetOutro=tweetOutro, tweetURL=tweetURL)

def assembleIntro():
    randIntro = randint(0,19)
    textIntro = [
    'MAGA TRUMP!','TRUMP 2020!','TRUMP America Great!','Keep America TRUMP!','TRUMP steaks great!','TRUMP Tower lu$$xury!','TRUMP #1!','So great TRUMP!','Handsomest Prez TRUMP!','TRUMP $$$!','$$ TRUMP so rich!','TRUMP the BEST!','TRUMP strong POWER!','TRUMPs handsome genes!','Clear WINNER!','TRUMP knows!','World\'s. Best. TRUMP!','My hero TRUMP!','Rename it TRUMPDAY!','Winning TRUMP!'
    ]
    return textIntro[randIntro]

def assembleMid():
    randMid = randint(0,29)
    textMid = [
    'jail time for you.','you\'re gonna die in prison.','your father never loved you.','your dad never cared about you.','DC lawyers all know you\'re poison.','you can\'t trust your men anymore.','impeached before long.','no lawyer is dumb enough to defend you now.','everyone knows you\'re poor.','you feel old and you look old.','we can all see you\'re horribly bald.','walls are closing in around you.','lawyers are too smart for you.','lawyers can smell your lies.','every old buddy is ratting on you this very moment.','your sons only want your money.','he only wants your money.','white house staff fleeing your sinking ship.','don jr dancing on your grave.','ivanka and jared are ratting on you.','lawyers are all jumping your sinking ship.','hope hicks is ratting on you now too.','ivanka talked to mueller can\'t trust her.','don jr talk to mueller can\'t trust him.','jared talked to mueller.','can\'t trust them better fire them.','can\'t even trust your bodyguards now.','they\'re coming for you.','they\'re going to get you in your sleep.','don\'t trust your bodyguards.']

    return textMid[randMid]

def assembleOutro():
    randOutro = randint(0,19)
    textOutro = [
    'TRUMP family 4ever!','TRUMP give em hell!','TrUmP!','TRUMP Richest Prez!','TRUMP Best Potus ever!','Trump Power!','TRUMP Muscle!','TRUMP America!','TRUMP America GREAT!','TRUMP Tower GOLD$$!','TRUMP $$!!','$$ TRUMP so rich!','TRUMP Tower $trong!','TRUMP America Great Again!','MAGA bitches!!','MAGA 2024!','MAGA Biggest fans!','TRUMP MAGA biggest ever!','MAGA 2020!','2020 TRUMP!'
    ]
    return textOutro[randOutro]



def assembleURL(tweetText):
    tweetText = re.sub(' ','%20',tweetText)
    tweetText = re.sub('!','%21',tweetText)
    tweetText = re.sub("'",'%27',tweetText)
    tweetText = re.sub('\.','%2E',tweetText)
    tweetText = re.sub('\$','%24',tweetText)
    tweetText = re.sub('#','%23',tweetText)

    urlToTweet='https://twitter.com/intent/tweet?&text=' + tweetText + '&tw_p=tweetbutton'

    return urlToTweet
