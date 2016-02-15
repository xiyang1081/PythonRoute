# -*- coding: utf-8 -*-

from flask import Flask,render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)


@app.route('/')
def index():
	# return "<h1>admin</h1>"
	return render_template('index.html')

if __name__ == '__main__':
	manager.run()