from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/ip')
def myip():
    return 'My IP is: '


if __name__ == '__main__':
    app.run()
