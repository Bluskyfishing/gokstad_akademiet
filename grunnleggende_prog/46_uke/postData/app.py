from flask import Flask, request, jsonify, render_template
import os 
from datetime import datetime

nowDate = datetime.today()

year = nowDate.strftime("%Y")
month = nowDate.strftime("%m")
day = nowDate.strftime("%d")
hour = nowDate.strftime("%H")
minute = nowDate.strftime("%M")
sec = nowDate.strftime("%S")



app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('submit.html')

@app.route('/submit', methods=['POST'])
def submitData():
    name = request.form.get('name')
    age = request.form.get('age')
    content = request.form.get('content')

    f = open(f"{name}_{age}_{year}-{month}-{day}_{hour}-{minute}-{sec}.txt", "w")
    f.write(content)
    f.close()

    return f"Name={name}, Age={age}, Content={content}"
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=7000)