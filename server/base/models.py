from django.db import models


class Property(models.Model):
	name = models.CharField(max_length=150)
	address = models.CharField(max_length=150)
	state = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=8)

	class Meta:
		verbose_name_plural = 'Properties'

