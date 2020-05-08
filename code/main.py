from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/hello2')
def hello2():
    return 'Hello from 2nd fucntion'


@app.route('/hello3')
def hello3():
    return 'Hello from 3rd function'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
