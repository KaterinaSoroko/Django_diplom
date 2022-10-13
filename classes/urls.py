from django.urls import path
from classes.views import page_class_view, ChoiseClassView, CreateClassView
from classes.views import UpdateClassesView, DeleteClassesView, UpdatePubClassesView


urlpatterns = [
    path('<int:class_id>', page_class_view, name='page_class'),
    path('create/', CreateClassView.as_view(), name='create_class'),
    path('update/<int:pk>', UpdateClassesView.as_view(), name='update_classes'),
    path('pupdate/<int:pk>', UpdatePubClassesView.as_view(), name='pub_classes'),
    path('delete/<int:pk>', DeleteClassesView.as_view(), name='delete_classes'),
    path('', ChoiseClassView.as_view(), name='choose_class'),
    ]
