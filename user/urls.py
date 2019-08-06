from django.urls import path
from django.conf.urls import include

from .views import SignUp, SignUpNormal, SignUpArtist

app_name = 'user'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpArtist.as_view(), name='signup'),
    path('signup/artist/', SignUpArtist.as_view(), name='artist_signup'),
    path('signup/normal/', SignUpNormal.as_view(), name='normal_signup'),
]