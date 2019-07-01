from django.db import models

# Create your models here.
class Product(models.Model):
	title		= models.CharField(max_length=50)
	description	= models.TextField()
	price		= models.TextField()
	summary		= models.TextField(default='This is')