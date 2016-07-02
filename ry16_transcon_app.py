from flask import Flask, render_template
from flask_compress import Compress

app = Flask(__name__)
Compress(app)


@app.route('/')
def hello_world():
    return render_template('ry16_transcon.html')

if __name__ == '__main__':
    app.run()
