from app import app
from flask import render_template


@app.route('/')
def index():
	name = 'Gellio'
	context = {
	'n': name
	}
	return render_template('index.html', context=context)