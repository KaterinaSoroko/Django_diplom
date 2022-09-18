from django.urls import path
from organization.views import create_org_view, page_org_view, choose_org_view


urlpatterns = [
    path('page/', page_org_view, name="page_org"),
    path('create/', create_org_view, name="create_org"),
    path('', choose_org_view, name="choose_org"),
    ]
