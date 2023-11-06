from flask import Flask, render_template
import random as rnd

app = Flask(__name__)

@app.route('/')
def showRandomNumber():
    rndNr = rnd.randint(1,100)
    return render_template("index.html", myRandomNumber=rndNr, numbers=[rnd.randint(1, 100) for _ in range(10)])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=7000)