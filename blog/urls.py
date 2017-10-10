from django.conf.urls import urls
from . import vivers

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
]