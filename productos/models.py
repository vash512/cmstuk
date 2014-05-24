from django.db import models
from shop.models import Product

class joya(Product):
	peso = models.DecimalField(max_digits=10, decimal_places=2)
	kilatage=models.DecimalField(max_digits=10, decimal_places=4)
	class Meta:pass