from wtforms import Form, StringField, TextAreaField, IntegerField, SelectField
from models import Currency


class CurrencyForm(Form):
	"""docstring for PostForm"""

	currency_name = StringField('Currency')
	currency_value = StringField('new_value')