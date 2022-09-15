from django.urls import path
from classes.views import page_class_view, create_class_view, choose_class_view


urlpatterns = [
    path('page-class/', page_class_view, name='page_class'),
    path('create-class/', create_class_view, name='create_class'),
    path('choose-class/', choose_class_view, name='choose_class'),
    ]
