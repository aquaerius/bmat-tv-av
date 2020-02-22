from django.conf.urls import url, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from core.views import logout_view
from core.views import home_view

app_name = 'core'
# For test will redirect straight to tv 
urlpatterns = [
	url(r'^$', login_required(home_view), name='home'),
	url(r'^login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
	url(r'^logout/', login_required(logout_view), name='logout'),
	url(r'^accounts/', include('django.contrib.auth.urls')),
	
]