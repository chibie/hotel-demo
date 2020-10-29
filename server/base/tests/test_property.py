import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Property, Booking
from ..serializers import PropertySerializer, BookingSerializer

client = Client()


class TestProperties(TestCase):
	"""
	Test module to GET all properties
	"""

	def setUp(self):
		Property.objects.create(
			name='R And A City Hotel', rating='3 star', address='2 Majekodunmi St, Allen, Ikeja',
			state='Lagos', price=32495
		)
		Property.objects.create(
			name='Lilygate Hotel', rating='4 star', address='2 Olubunmi Owa St, Lekki Phase I, Lagos',
			state='Lagos', price=38696
		)
		Property.objects.create(
			name='The Edge By Wellness', rating='4 star', address='Citec Villa, 1, C-Close, 4th Ave, Gwarinpa 900108, Abuja',
			state='Abuja', price=13438
		)
	
	def test_get_all_properties(self):
		response = client.get(reverse('properties'))
		properties = Property.objects.all()
		serializer = PropertySerializer(properties, many=True)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestPropertyBookings(TestCase):
	"""
	Test module to GET all Bookings for a Property
	"""

	def setUp(self):
		property = Property.objects.create(
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

	def test_get_all_bookings_of_a_property(self):
		response = client.get(reverse('properties_booked', kwargs={'id': 1}))
		bookings = Property.objects.get(id=1).booking.all()
		serializer = BookingSerializer(bookings, many=True)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
