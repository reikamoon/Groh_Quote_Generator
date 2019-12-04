from flask import Flask, render_template, request
import random
from Code.generate import *

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')
    

@app.route('/results')
def results():
    quotes = ["This, too is my mission!", "Outsider encountered, neutralizing threat.", "My mission is what matters, not you.", "Chevalier...mal fet!", "Nimue's Embrace!", "Sire Balin's Swords!", "Astolat's Echo!", "All I have to say...is die.", "You shall be judged...in hell.", "Your existence is a danger.", "Loengrin's Courage!", "Fear my blade!", "I care not for my seat in the twelve.", "Scarlet Sleeve!", "Gallatin Eclipse!", "The Path, to Avalon!", "Guinevere's Indiscretion!", "I shall succeed!", "I know your game.", "Atone for the sin of weakness.", "Begone. You are no threat to me.", "Is that all you have?", "I will...KILL YOU!", "Come at me, Outsider!", "Outsiders are evil. They must die.", "So Naive...", "Rue, your weakness!", "A storm is coming!", "Endless quest!", "Roar for me, Arondight!", "Coup de Main!", "Limitless!", "Instant Death!", "Lightning slash!", "Lightning Slash! You're mine...Camelot's Ruse!", "Go forth, Guilt Seeker!", "I shall leave no trace.", "You will be erased!", "Allow me to demonstrate.", "Speed up!", "Following up!", "Wasteland!", "Special Attack!", "Deploy!", "Part!", "Separate!", "It's over!", "DAMN YOU!", "Ever the monsterous wretch!", "You will pay for all you have done!", "My wound ACHES!", "Do not hold back, however, I will", "I shall succeed!", "Rot away. Your fate is decided.", "Kill me!", "The rest is in your hands."]
    quote = random.choice(quotes)
    return render_template('results.html', quote=quote)





    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
