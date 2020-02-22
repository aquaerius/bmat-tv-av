from .views import ChannelDetailView
from .views import ChannelListView
from .views import ProgramDetailView
from .views import ProgramListView
from .views import ShowtimeDetailView
from .views import showtimes_view
from .views import ChannelViewSet, ProgramViewSet

from django.contrib.auth.decorators import login_required
from django.conf.urls import url, include
from rest_framework import routers

app_name = 'tv'

router = routers.DefaultRouter()
router.register(r'^channel', ChannelViewSet)
router.register(r'^program', ProgramViewSet)

urlpatterns = [
    url(r'^programs/', login_required(ProgramListView.as_view()), name='programs'),
    url(r'^programs/<int:pk>/', login_required(ProgramDetailView.as_view()), name='program-detail'),
    url(r'^programs/showtime/<int:pk>/', login_required(ShowtimeDetailView.as_view()), name='showtimes'),
    url(r'^showtimes/', login_required(showtimes_view), name='showtime-lists'),
    url(r'^channels/', login_required(ChannelListView.as_view()), name='channels'),
    url(r'^channels/<int:pk>/', login_required(ChannelDetailView.as_view()), name='channel-detail'),
    url(r'^v1/', include(router.urls)),  # TV API endpoint
    url(r'^v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
]
