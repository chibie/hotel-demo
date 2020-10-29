from django.urls import path
from .views import BookingCreate, PropertyBookedList
from rest_framework.documentation import include_docs_urls

urlpatterns = [
	path('bookings/', BookingCreate.as_view(), name='bookings'),
	path('properties/<int:id>/bookings/', PropertyBookedList.as_view(), name='properties_booked'),
    path('docs/', include_docs_urls(title='Properties API Documentation'), name='docs')
]