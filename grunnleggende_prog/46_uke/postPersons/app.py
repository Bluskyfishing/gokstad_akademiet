from flask import Flask, request, jsonify, render_template
import reading_file
import json

app = Flask(__name__)

@app.route('/')
def showPersonDataJSON():
    persons = reading_file.read_persons("persons.csv", True)
    personListjson = [dict(zip(persons[0], person)) for person in persons[1:]]
    personjson = json.dumps(personListjson)
    return render_template("table.html", persons=json.loads(personjson))

@app.route('/add', methods=['POST'])
def addperson():
    return render_template("addperson.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=7000)