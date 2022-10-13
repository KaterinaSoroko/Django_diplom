from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
from Fanipol.views import fanipol_view, registration_view, no_access_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', registration_view, name='registration'),
    path('user/', include('user.urls')),
    path('org/', include('organization.urls')),
    path('class/', include('classes.urls')),
    path('evenv/', include('event.urls')),
    path('no_access/', no_access_view, name='no_access'),
    path('', fanipol_view, name='about_fanipol')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
