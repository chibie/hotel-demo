from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .models import Property, Booking
from .serializers import PropertySerializer, BookingSerializer


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

