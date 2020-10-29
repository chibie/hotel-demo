from django.db import models


class Property(models.Model):
	name = models.CharField(max_length=150)
	rating = models.CharField(max_length=10)
	address = models.CharField(max_length=150)
	state = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=8, decimal_places=2)

	class Meta:
		verbose_name_plural = 'Properties'

	def __str__(self):
		return f'{self.name}'


class Booking(models.Model):
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	email = models.EmailField(max_length=150, unique=True)
	property_booked = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='booking')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = 'Bookings'
