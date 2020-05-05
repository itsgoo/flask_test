import requests
from bs4 import BeautifulSoup
import csv


main_url = 'https://fx-rate.net/'
postfix = 'dollar+to+shekel'
# dollar+to+shekel
# shekel+to+rubble


def get_html(url):
	r = requests.get(url, )
	return r.text



def ready_url(url, new_currency):
	# https://fx-rate.net
	# new_currency = '/USD/ILS/'
	# new_currency = '/ILS/RUB/'
	ready = url + new_currency
	return ready



def get_content(ready_url):

	url_html= get_html(ready_url)
	soup = BeautifulSoup(url_html, 'lxml')
	
	# value = soup.find('form', class_='todaycurrencycalculator').find('table').find('tbody').find_all('tr').find_all('fieldset').find('input' class_='ip_amount cal_amount_from').get(value)
	value_from = soup.find('input', class_='ip_amount cal_amount_from').get('value')
	value_to = soup.find('input', class_='ip_amount cal_amount_to').get('value')


	value_to = float(value_to)
	value_from = float(value_from)


	value_clean = value_to/value_from

	
	return value_clean





def reverce_val(query):

	mass_dates = []
	for i in query:
		mass_dates.append(str(i.currency_date.strftime('%d %H-%M')))

	mass_dates_rev = []
	for i in reversed(mass_dates):
		mass_dates_rev.append(i)



	mass_currency = []
	for i in query:
		mass_currency.append(i.currency_value)

	mass_currency_rev = []
	for i in reversed(mass_currency):
		mass_currency_rev.append(i)

	return mass_dates_rev, mass_currency_rev

