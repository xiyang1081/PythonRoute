# -*- coding: utf-8 -*-

from flask import Flask,request,redirect
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	return '<h1>Hello,world!</h1><h2>%s</h2>' % user_agent

@app.route('/user/<username>')
def get_user(username):
	return '<h1>username:%s</h1>' % username

@app.route('/hello')
def hello():
	return redirect('http://www.baidu.com')

if __name__ == '__main__':
	# app.run(debug=True)
	manager.run()