from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.RestaurantListView.as_view(), name="list"),
    url(r'^(?P<slug>[-\w]+)/$', views.RestaurantDetailView.as_view(), name="detail"),
    url(r'^create/$', views.RestaurantCreateView.as_view(), name="create"),
    url(r'^(?P<slug>[-\w]+)/delete/$', views.RestaurantDeleteView.as_view(), name="delete"),
    url(r'^(?P<slug>[-\w]+)/update/$', views.RestaurantUpdateView.as_view(), name="update"),
]
