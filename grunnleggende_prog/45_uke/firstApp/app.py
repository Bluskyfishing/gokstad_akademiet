from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/hello')
def hello():
    return "helo"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=7000)