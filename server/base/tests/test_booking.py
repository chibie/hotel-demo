import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Property, Booking
from ..serializers import BookingSerializer

client = Client()

class GetAllBookingsTest(TestCase):
	"""
	Test module to GET all bookings
	"""

	def setUp(self):
		property = 	Property.objects.create(
			name='R And A City Hotel', rating='3 star', address='2 Majekodunmi St, Allen, Ikeja',
			state='Lagos', price=32495
		)
		Booking.objects.create(
			first_name='Yagami', last_name='Light',
			email='yagami@lightmail.com', property_booked=property
		)
		Booking.objects.create(
			first_name='Ilumi', last_name='Zoldyck',
			email='ilumi@zoldyckmail.com', property_booked=property
		)
		Booking.objects.create(
			first_name='Chairman', last_name='Netero',
			email='chairman@neteromail.com', property_booked=property
		)

	def test_get_all_properties(self):
		response = client.get(reverse('bookings'))
		bookings = Booking.objects.all()
		serializer = BookingSerializer(bookings, many=True)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateNewBookingTest(TestCase):
	"""
	Test module to POST a new Booking instance
	"""

	def setUp(self):
		property = Property.objects.create(
			name='Lilygate Hotel', rating='4 star', address='2 Olubunmi Owa St, Lekki Phase I, Lagos',
			state='Lagos', price=38696
		)
		self.payload = {
			'first_name': 'Commander',
			'last_name': 'Erwin',
			'email': 'erwin@commandmail.com',
			'property_booked': property.id
		}

	def test_create_new_booking(self):
		response = client.post(
			reverse('bookings'), data=json.dumps(self.payload), content_type='application/json' 
		)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
