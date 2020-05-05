from flask import Blueprint
from flask import render_template

from models import Currency
from .forms import CurrencyForm

from flask import request
from app import db

from flask import redirect
from flask import url_for

from functions import *


dashbord = Blueprint('dashbord', __name__, template_folder ='templates' )


@dashbord.route('/', methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':






		new_currency = request.form['currency_name']
		funcstart = get_content(ready_url(main_url, new_currency))
		print(funcstart)

		new_value = round(float(funcstart), 3)

		print(new_value)

		try:
			currency_note = Currency(currency_name = new_currency, currency_value = new_value)
			db.session.add(currency_note)
			db.session.commit()
		except:
			print('something went wrong')
		return redirect(url_for('dashbord.index'))

	else:
		form = CurrencyForm()

		graph_usd_to_ils = Currency.query.filter(Currency.currency_name == '/USD/ILS/').order_by(db.desc(Currency.currency_date)).limit(7)

		graph_ils_to_rub = Currency.query.filter(Currency.currency_name == '/ILS/RUB/').order_by(db.desc(Currency.currency_date)).limit(7)
		


		mass_dates_rev_u_i, mass_currency_rev_u_i = reverce_val(graph_usd_to_ils)


		mass_dates_rev_i_r, mass_currency_rev_i_r = reverce_val(graph_ils_to_rub)



		return render_template('dashbord/index.html', 
			form = form, 
			currency_usd_to_ils = graph_usd_to_ils,
			currency_ils_to_rub = graph_ils_to_rub, 

			mass_dates = mass_dates_rev_u_i, 
			mass_currency = mass_currency_rev_u_i, 

			mass_dates_2 = mass_dates_rev_i_r, 
			mass_currency_2 = mass_currency_rev_i_r, 
			)



