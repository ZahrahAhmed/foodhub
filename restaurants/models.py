from django.db import models

class Restaurant(models.Model):
	name =models.CharField(max_length=220)
	description = models.TextField()
	opening_time= models.TimeField()
	closing_time= models.TimeField()
	logo=  models.ImageField(null=True , blank=True, upload_to="restaurant_images")

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']