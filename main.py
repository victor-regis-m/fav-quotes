from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qarwecwthxjrsc:9d16d7b1b21a0806211c622eecbc2d634c2f06f0e8d2c777e55b2ba5533c37d8@ec2-44-210-36-247.compute-1.amazonaws.com:5432/d67ohdtsde96ar'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Favquotes (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result =  Favquotes.query.all()
    return render_template('index.html', result = result)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process', methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author = author, quote = quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))
