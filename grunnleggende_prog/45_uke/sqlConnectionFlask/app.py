from flask import Flask, render_template
import findEverythingInColumn
import json

app = Flask(__name__)


@app.route('/')
def showNordicCountries():
    ncountry = findEverythingInColumn.selectEverything()
    return render_template("nordicCountries.html", ncountry=ncountry)

@app.route('/test')
def test():
    return render_template("test.html")

#@app.route('/json')
#def showPersonDataJSON():
#    
#    countriesListjson = [dict(zip(countries[0], country)) for country in countries[1:]]
#    countryjson = json.dumps(countriesListjson)
#    return render_template("nordicCountries.html", ncountry=json.loads(countryjson))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=7000)