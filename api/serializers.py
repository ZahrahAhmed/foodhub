from rest_framework import serializers
from restaurants.models import Restaurant

class RestaurantListSerializer(serializers.ModelSerializer):
	x = serializers.HyperlinkedIdentityField(
		view_name="api:detail",
		lookup_field="slug",
		lookup_url_kwarg="slug"
		)

	class Meta:
		model = Restaurant 
		fields = ['name','logo','opening_time', 'closing_time','x']

class RestaurantDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ['id','name', 'description','logo','opening_time', 'closing_time', 'slug']

class RestaurantCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ['name','logo','opening_time', 'closing_time', 'description']
