import random
import requests
from ..models import Property

BASE_URL = 'https://discover.search.hereapi.com/v1/discover'


def fetch_hotels(long, lat, query, limit, api_key):
	hotels = []
	url = f'{BASE_URL}?at={long},{lat}&q={query}&limit={limit}&apiKey={api_key}'
	request = requests.get(url)
	response = request.json()['items']
	
	for hotel in response:
		hotelDict = {
			'title': hotel['title'],
			'address': hotel['address']['label'],
			'state': hotel['address']['state'],
			'position': {
				'lng': hotel['position']['lng'],
				'lat': hotel['position']['lat']
			},
			'price': random.randrange(100, 200),
		}

		hotels.append(hotelDict)

	return hotels

	name = models.CharField(max_length=150)
	rating = models.CharField(max_length=10)
	address = models.CharField(max_length=150)
	state = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=8, decimal_places=2)
