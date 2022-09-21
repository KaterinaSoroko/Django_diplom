from django.contrib import admin
from django.urls import path, include
from Fanipol.views import fanipol_view, registration_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', registration_view, name='registration'),
    path('user/', include('user.urls')),
    path('org/', include('organization.urls')),
    path('class/', include('classes.urls')),
    path('evenv/', include('event.urls')),
    path('', fanipol_view, name='about_fanipol'),
]
