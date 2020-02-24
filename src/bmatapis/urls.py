from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from rest_framework.authtoken.views import obtain_auth_token

from core import urls as core_urls
from tv import urls as tv_urls
from rest_framework import routers
from tv import views as tv_views


router = routers.DefaultRouter()
router.register(r'programs', tv_views.ShowtimeViewSet)
router.register(r'channels', tv_views.ChannelViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^', include(core_urls)), 
    url(r'^tv/', include(tv_urls)),
    url(r'^tv/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_auth_token, name='api_token_auth')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
