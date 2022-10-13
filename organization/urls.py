from django.urls import path
from organization.views import CreateOrgView, page_org_view, ChoiceOrgView
from organization.views import UpdateOrgView, DeleteOrgView, UpdatePubOrgView

urlpatterns = [
    path('<int:pk>/', page_org_view, name="page_org"),
    path('create/', CreateOrgView.as_view(), name="create_org"),
    path('update/<int:pk>', UpdateOrgView.as_view(), name = "update_org"),
    path('pupdate/<int:pk>', UpdatePubOrgView.as_view(), name="pub_org"),
    path('delete/<int:pk>', DeleteOrgView.as_view(), name='delete_org'),
    path('', ChoiceOrgView.as_view(), name="choice_org"),
    ]
