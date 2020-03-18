from flask import Flask, render_template, Response
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', name='Sol')


@app.route('/ip')
def myip():
    return Response(body='My IP is:', status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
