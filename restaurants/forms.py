from django import forms
from .models import Restaurant, Item
from django.contrib.auth.models import User 


class RestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ['name','description', 'opening_time', 'closing_time', 'logo'] 
		
class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['active', 'price', 'name', 'restaurant']

class UserSignup(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password'] 

		widgets={
		'password': forms.PasswordInput(),
		}

class UserLogin(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())
