from django.shortcuts import render, get_object_or_404
from organization.models import Organization


def create_org_view(request):
    return render(request, 'create_org.html', {})


def page_org_view(request, pk):
    org_list = get_object_or_404(Organization, pk=pk)
    return render(request, 'page_org.html', {"org": org_list})


def choose_org_view(request):
    org_list = Organization.objects.all()
    return render(request, 'choose_org.html', {"orgs": org_list})
