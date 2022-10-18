from django.urls import path
from event.views import ChoiceEventView, PageEventView, CreateEventView
from event.views import UpdateEventView, DeleteEventView, UpdatePubEventView


urlpatterns = [
    path('<int:pk>', PageEventView.as_view(), name='page_event'),
    path('create/', CreateEventView.as_view(), name='create_event'),
    path('update/<int:pk>', UpdateEventView.as_view(), name='update_event'),
    path('pupdate/<int:pk>', UpdatePubEventView.as_view(), name='pub_event'),
    path('delete/<int:pk>', DeleteEventView.as_view(), name='delete_event'),
    path('', ChoiceEventView.as_view(), name='choice_event'),
    ]
