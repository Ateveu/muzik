from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from user.views import SignUpArtist, SignUpNormal, SignUp

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include('events.urls')),
    path('accounts/', include('user.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)