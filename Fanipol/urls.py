from django.contrib import admin
from django.urls import path, include
from Fanipol.views import fanipol_view, registration_view, user_view, create_user_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', registration_view, name='registration'),
    path('create-user/', create_user_view, name='create_user'),
    path('user/', user_view, name='user'),
    path('page-org/', include('organization.urls')),
    path('create-org/', include('organization.urls')),
    path('choose-org/', include('organization.urls')),
    path('page-class/', include('classes.urls')),
    path('create-class/', include('classes.urls')),
    path('choose-class/', include('classes.urls')),
    path('page-evenv/', include('event.urls')),
    path('create-event/', include('event.urls')),
    path('choose-event/', include('event.urls')),
    path('', fanipol_view, name='about_fanipol'),

]
