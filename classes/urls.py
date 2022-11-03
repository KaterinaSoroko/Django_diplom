from django.urls import path
from classes.views import page_class_view, ChoiseClass1View, CreateClassView, DeleteAgeView, create_age_view
from classes.views import UpdateClassesView, DeleteClassesView, UpdatePubClassesView, DeletePhotoView


urlpatterns = [
    path('<int:class_id>', page_class_view, name='page_class'),
    path('create/', CreateClassView.as_view(), name='create_class'),
    path('<int:pk>/update/', UpdateClassesView.as_view(), name='update_classes'),
    path('<int:pk>/publication/', UpdatePubClassesView.as_view(), name='pub_classes'),
    path('<int:pk>/create_age/', create_age_view, name='create_age'),
    path('<int:pk>/delete/', DeleteClassesView.as_view(), name='delete_classes'),
    path('<int:class_id>/delete_photo/<int:pk>', DeletePhotoView.as_view(), name="delete_photo"),
    path('<int:class_id>/delete_age/<int:pk>', DeleteAgeView.as_view(), name="delete_age"),
    path('', ChoiseClass1View.as_view(), name='choose_class'),
    ]
