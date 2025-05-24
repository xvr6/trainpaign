from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/hello')
def hello():
    return 'Hello, Flask!'

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')