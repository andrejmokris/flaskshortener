from flask import Flask, render_template, redirect, request, jsonify
import random
import string

app = Flask(__name__)

dic = {"google": 'https://www.google.com', "fb": 'https://www.facebook.com', "gbas": "https://www.gbas.edupage.org"}

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
	long_url = request.form['text']
	short_url = request.form['want']
	dic[short_url] = long_url
	return index()

@app.route("/<url>", methods=['GET', 'POST'])
def short(url):
	return redirect(dic[url])

@app.route('/all')
def show_all():
	return jsonify(dic)

if __name__ == "__main__":
	app.run()