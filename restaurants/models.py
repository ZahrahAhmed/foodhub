from django.db import models
from django.db.models.signals import pre_save 
from django.template.defaultfilters import slugify



class Restaurant(models.Model):
	name =models.CharField(max_length=220, unique=True)
	description = models.TextField()
	opening_time= models.TimeField()
	closing_time= models.TimeField()
	logo=  models.ImageField(null=True , blank=True, upload_to="restaurant_images")
	slug = models.SlugField(blank =True)


	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']

def presf(*args, **kwargs):
	y = kwargs['instance']
	y.slug = slugify(y.name)

pre_save.connect(presf, sender=Restaurant)

class Item(models.Model):
	restaurant = models.ForeignKey(Restaurant)
	name = models.CharField(max_length=220, unique=True)
	slug = models.SlugField(blank =True)
	description = models.TextField()
	price = models.DecimalField(max_digits=20 , decimal_places=3)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']


def presf2(*args, **kwargs):
	y = kwargs['instance']
	y.slug = slugify(y.name)

pre_save.connect(presf2, sender=Item)