from django.urls import path
from classes.views import page_class_view, create_class_view, choose_class_view


urlpatterns = [
    path('page/', page_class_view, name='page_class'),
    path('create/', create_class_view, name='create_class'),
    path('', choose_class_view, name='choose_class'),
    ]
