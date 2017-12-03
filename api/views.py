from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from restaurants.models import Restaurant
from .serializers import RestaurantListSerializer, RestaurantDetailSerializer, RestaurantCreateUpdateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.filters import SearchFilter

class RestaurantListView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer
	permission_classes=[AllowAny]
	filter_backends = [SearchFilter,]
	search_fields = ['name', 'description']


class RestaurantDetailView(RetrieveAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantDetailSerializer
	lookup_field = "slug"
	lookup_url_kwarg="slug"
	permission_classes=[IsAuthenticated,]

class RestaurantDeleteView(RetrieveAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer
	lookup_field = "slug"
	lookup_url_kwarg="slug"
	permission_classes=[IsAuthenticated, IsAdminUser]

class RestaurantUpdateView(RetrieveUpdateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantCreateUpdateSerializer
	lookup_field = "slug"
	lookup_url_kwarg="slug"
	permission_classes=[IsAuthenticated,]

class RestaurantCreateView(CreateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantCreateUpdateSerializer
	permission_classes=[IsAuthenticated,]