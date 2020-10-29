from django.urls import path
from .views import BookingCreate, PropertyBookedList

urlpatterns = [
	path('bookings/', BookingCreate.as_view(), name='bookings'),
	path('properties/<int:id>/bookings/', PropertyBookedList.as_view(), name='properties_booked')
]