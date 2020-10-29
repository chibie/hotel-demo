from django.urls import path
from .views import PropertyList, BookingCreate, PropertyBookedList
from rest_framework.documentation import include_docs_urls

urlpatterns = [
	path('properties/', PropertyList.as_view(), name='properties'),
	path('bookings/', BookingCreate.as_view(), name='bookings'),
	path('properties/<int:id>/bookings/', PropertyBookedList.as_view(), name='properties_booked'),
	path('docs/', include_docs_urls(title='Properties API Documentation'), name='docs')
]
