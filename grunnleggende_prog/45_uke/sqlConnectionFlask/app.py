from flask import Flask, render_template
#import reading_file
import json
import mysql.connector

app = Flask(__name__)

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="test",
    database="world"
)

myCursor = myDB.cursor()
myCursor.execute("SHOW TABLES")
tables = myCursor.fetchall() #same as ; its just to run another query 

@app.route('/')
def showNordicCountries():
    return render_template("nordicCountries.html", countries=ncountries)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=7000)