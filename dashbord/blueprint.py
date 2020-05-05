from flask import Blueprint
from flask import render_template

from models import Currency
from .forms import CurrencyForm

from flask import request
from app import db

from flask import redirect
from flask import url_for

dashbord = Blueprint('dashbord', __name__, template_folder ='templates' )


@dashbord.route('/', methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		new_currency = request.form['currency_name']
		new_value = request.form['currency_value']
		try:
			currency_note = Currency(currency_name = new_currency, currency_value = new_value)
			db.session.add(currency_note)
			db.session.commit()
		except:
			print('something went wrong')
		return redirect(url_for('dashbord.index'))

	else:
		form = CurrencyForm()
		currency = Currency.query.all()


		return render_template('dashbord/index.html', form = form, currency = currency, )



