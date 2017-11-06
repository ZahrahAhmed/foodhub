from django.shortcuts import render
from .models import Restaurant

def restaurant_list(request):
	context = {
	"objects": Restaurant.objects.all(),
	}
	return render(request, "restaurant_list.html", context)

def restaurant_detail(request, restaurant_id):
	context = {
	"object": Restaurant.objects.get(id=restaurant_id),
	}
	return render(request, "restaurant_detail.html", context)


