from django.shortcuts import render
from django.conf import settings
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Property, Booking
from .serializers import PropertySerializer, BookingSerializer
from .utils.fetch_hotels import fetch_hotels


class PropertyList(APIView):
	"""
	Return all instances of the Property model.
	If URL contains an `at` query string, return results from HERE Places API.
	"""
	def get(self, request):
		if 'at' in self.request.GET:
			lat, long = self.request.GET.get('at').split(',')
			hotels = fetch_hotels(lat, long, 'hotel', 5, settings.HERE_API_KEY)
			return Response(hotels)
		else:
			properties = Property.objects.all()
			data = PropertySerializer(properties, many=True).data
			return Response(data)


class BookingCreate(ListCreateAPIView):
	"""
	get:
	Return all instances of the Booking model.

	post:
	Create a new Booking instance.
	"""
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer


class PropertyBookedList(ListAPIView):
	"""
	Return a list of all Bookings corresponding to a Property.
	"""
    serializer_class = BookingSerializer

	def get_queryset(self):
		queryset = Property.objects.get(id=self.kwargs['id']).booking.all()
		return queryset

