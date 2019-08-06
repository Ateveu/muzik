from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url, include

from config import settings
from .views import HomePageView, create_event,events_list

urlpatterns = [
    path('', events_list, name='home'),
    path('event/', create_event, name='add_event'),
]