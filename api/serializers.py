from rest_framework import serializers
from restaurants.models import Restaurant, Item

class ItemListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name="api:itemdetail",
		lookup_field="slug",
		lookup_url_kwarg="slug"
		)
	class Meta:
		model = Item
		fields = ["name", "price", "active", "detail"]

class ItemDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = Item
		fields = ["id", "restaurant", "name", "slug", "description", "price", "active",]

class RestaurantListSerializer(serializers.ModelSerializer):
	detail_page = serializers.HyperlinkedIdentityField(
		view_name="api:detail",
		lookup_field="slug",
		lookup_url_kwarg="slug"
		)

	class Meta:
		model = Restaurant 
		fields = ['name','logo','opening_time', 'closing_time','detail_page']

class RestaurantDetailSerializer(serializers.ModelSerializer):
	items = serializers.SerializerMethodField()
	class Meta:
		model = Restaurant
		fields = ['id','name', 'description','logo','opening_time', 'closing_time', 'slug', 'items']

	def get_items(self, obj):
		item_list = Item.objects.filter(restaurant=obj)
		items = ItemListSerializer(item_list, many=True, context=self.context).data
		return items


class RestaurantCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ['name','logo','opening_time', 'closing_time', 'description']
