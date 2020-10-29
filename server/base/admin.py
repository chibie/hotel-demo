from django.contrib import admin
from .models import Property, Booking


class PropertyAdmin(admin.ModelAdmin):
	list_display = ('name', 'id', 'address')
	list_filter = ('name', 'state')
	search_fields = ('name', 'state')


class BookingAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'id', 'last_name', 'property_booked', 'created')
	list_filter = ('first_name', 'last_name', 'property_booked')
	search_fields = ('first_name', 'last_name', 'property_booked')
	raw_id_fields = ('property_booked',)


admin.site.register(Property, PropertyAdmin)
admin.site.register(Booking, BookingAdmin)
