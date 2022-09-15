from django.urls import path
from event.views import page_event_view, create_event_view, choose_event_view


urlpatterns = [
    path('page-evenv/', page_event_view, name='page_event'),
    path('create-event/', create_event_view, name='create_event'),
    path('choose-event/', choose_event_view, name='choose_event'),
    ]
