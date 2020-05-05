from wtforms import Form, StringField, TextAreaField, IntegerField, SelectField
from models import Currency


class CurrencyForm(Form):
	"""docstring for PostForm"""


	currency_name = SelectField(u'Currency', choices=[
		('/USD/ILS/','USD to ILS'), 
		('/ILS/RUB/','ILS to RUB'), 
		])