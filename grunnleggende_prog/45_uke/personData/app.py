from flask import Flask, render_template
import random as rnd
import reading_file
import json

app = Flask(__name__)

@app.route('/')
def showPersonData():
    persons = reading_file.read_persons("persons.csv")
    return render_template("personData.html", persons=persons)


@app.route('/json')
def showPersonDataJSON():
    persons = reading_file.read_persons("persons.csv", True)
    personListjson = [dict(zip(persons[0], person)) for person in persons[1:]]
    personjson = json.dumps(personListjson)
    return render_template("personDataJSON.html", persons=json.loads(personjson))

@app.route('/test')
def test():
    return render_template("test.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=7000)