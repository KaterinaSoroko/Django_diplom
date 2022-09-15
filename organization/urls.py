from django.urls import path
from organization.views import create_org_view, page_org_view, choose_org_view


urlpatterns = [
    path('organization/', page_org_view, name="page_org"),
    path('create_org/', create_org_view, name="create_org"),
    path('choose_org/', choose_org_view, name="choose_org"),
    ]
