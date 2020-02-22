from django.conf.urls import url

from core import views as core_views

app_name = 'core'

urlpatterns = [
	url(r'^$', core_views.home, name='home'),	
]
