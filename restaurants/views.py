from django.shortcuts import render, redirect
from .models import Restaurant, Item
from .forms import RestaurantForm, ItemForm, UserLogin, UserSignup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate 

def usersignup(request):
	x = UserSignup()
	context = {"x": x, }
	if request.method=="POST":
		x = UserSignup(request.POST)
		if x.is_valid():
			y = x.save()
			username = y.username
			password = y.password

			y.set_password(password)
			y.save()
			auth = authenticate(username=username, password=password)
			login(request, auth)
			messages.warning(request, 'you have successfuly signed up!')
			return redirect("restaurant_list")
		else:
			messages.warning(request, x.errors)
			return redirect("usersignup")
	return render(request,"signup.html", context)

def userlogin(request):
	x = UserLogin()
	context = {"x": x, }
	if request.method=="POST":
		x = UserLogin(request.POST)
		if x.is_valid():
			someusername = x.cleaned_data['username']
			somepassword = x.cleaned_data['password']

			auth = authenticate(username=someusername, password=somepassword)

			if auth is not None:
				login(request, auth)
				messages.warning(request, 'you have successfuly logged in!')
				return redirect("restaurant_list")
			else:
				messages.warning(request, 'Incorrect UserName/Password combination.')
				return redirect("userlogin")
		else:
			messages.warning(request, x.errors)
			return redirect("userlogin")

	return render(request,"login.html", context)

def userlogout(request):
	logout(request)
	return redirect("userlogin")
	messages.warning(request, 'you have successfuly logged out!')


def item_create(request):
	if not request.user.is_staff:
		raise Http404
	x = ItemForm(request.POST or None)
	if x.is_valid():
		x.save()
		return redirect("restaurant_list")

	context = {"x": x, }
	return render(request, "item_create.html", context)

def item_update(request, item_slug):
	if not request.user.is_staff:
		raise Http404
	y = Item.objects.get(slug=item_slug)
	x = ItemForm(request.POST or None, instance=y)
	if x.is_valid():
		x.save()
		return redirect("restaurant_detail", item_slug=y.slug)
	context = { 
	"y": y,
	"x" : x,
	 }
	return render(request, "item_update.html", context)

def item_delete(request, item_slug):
	if not request.user.is_staff:
		raise Http404
	Item.objects.get(slug=item_slug).delete()
	return redirect("restaurant_list")

def restaurant_detail(request, restaurant_slug):
	status = "open"
	restaurant = Restaurant.objects.get(slug=restaurant_slug)
	items = Item.objects.filter(restaurant=restaurant)

	if not request.user.is_staff:
		items = items.filter(active=True)

	if timezone.now().time() < restaurant.opening_time or timezone.now().time() > restaurant.closing_time:
		status = "closed"

	context = {
		"status":status,
		"restaurant": restaurant,
		"items": items,
	}
	return render(request, 'restaurant_detail.html', context)

def restaurant_list(request):
	object_list = Restaurant.objects.all()

	query = request.GET.get("q")
	if query:
		object_list = object_list.filter(name__icontains=query)

	paginator = Paginator(object_list, 5)
	page = request.GET.get('page')
	try:
		objects = paginator.page(page)
	except PageNotAnInteger:
		objects = paginator.page(1)
	except EmptyPage:
		objects = paginator.page(paginator.num_pages)

	context = {
		"objects":objects,
	}
	return render(request, 'restaurant_list.html', context)


def restaurant_create(request):
	if not request.user.is_staff:
		raise Http404
	x = RestaurantForm(request.POST or None, request.FILES or None)
	if x.is_valid():
		x.save()
		return redirect("restaurant_list")
	context = { "x": x, }
	return render(request, "restaurant_create.html", context)

def restaurant_update(request, restaurant_slug):
	if not request.user.is_staff:
		raise Http404
	y = Restaurant.objects.get(slug=restaurant_slug)
	x = RestaurantForm(request.POST or None, request.FILES or None, instance=y)
	if x.is_valid():
		x.save()
		return redirect("restaurant_detail", restaurant_slug=y.slug)
	context = {
		"x": x,
		"y": y, }
	return render(request, "restaurant_update.html", context)

def restaurant_delete(request, restaurant_slug):
	if not request.user.is_staff:
		raise Http404
	Restaurant.objects.get(slug=restaurant_slug).delete()
	return redirect("restaurant_list")

