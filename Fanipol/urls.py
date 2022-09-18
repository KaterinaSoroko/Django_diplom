from django.contrib import admin
from django.urls import path, include
from Fanipol.views import fanipol_view, registration_view, user_view, create_user_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', registration_view, name='registration'),
    path('create-user/', create_user_view, name='create_user'),
    path('user/', user_view, name='user'),
    path('org/', include('organization.urls')),
    path('class/', include('classes.urls')),
    path('evenv/', include('event.urls')),
    path('', fanipol_view, name='about_fanipol'),

]
