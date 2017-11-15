from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def restaurant_list(request):
	objects=Restaurant.objects.all()
	paginator = Paginator(objects, 2)
	page = request.GET.get('page')
	try:
		objects = paginator.page(page)
	except PageNotAnInteger:
		objects = paginator.page(1)
	except EmptyPage:
		objects = paginator.page(paginator.num_pages)
	context = {
	"objects": objects,
	}
	return render(request, "restaurant_list.html", context)

def restaurant_detail(request, restaurant_id):
	context = {
	"object": Restaurant.objects.get(id=restaurant_id),
	}
	return render(request, "restaurant_detail.html", context)

def restaurant_create(request):
	x = RestaurantForm(request.POST or None, request.FILES or None)
	if x.is_valid():
		x.save()
		return redirect("restaurant_list")
	context = { "x": x, }
	return render(request, "restaurant_create.html", context)

def restaurant_update(request, restaurant_id):
	y = Restaurant.objects.get(id=restaurant_id)
	x = RestaurantForm(request.POST or None, request.FILES or None, instance=y)
	if x.is_valid():
		x.save()
		return redirect("restaurant_detail", restaurant_id=y.id)
	context = {
		"x": x,
		"y": y, }
	return render(request, "restaurant_update.html", context)

def restaurant_delete(request, restaurant_id):
	Restaurant.objects.get(id=restaurant_id).delete()
	return redirect("restaurant_list")

