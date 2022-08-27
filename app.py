from flask import Flask, render_template, request
import tensorflow as tf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # versi = tf.__version__
    # return render_template('home.html', kata=versi)
    return render_template('home.html', kata="Hublaa")

if __name__ == '__main__':
    app.run()