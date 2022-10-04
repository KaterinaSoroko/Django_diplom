from django.shortcuts import render, get_object_or_404
from organization.models import Organization
from organization.forms import OrganizationForm
from classes.models import Class
from event.models import Event


def create_org_view(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
    else:
        form = OrganizationForm()
    content = {"org_form": form}
    return render(request, 'create_org.html', content)


def page_org_view(request, pk):
    org_list = get_object_or_404(Organization, pk=pk)
    class_list = Class.objects.filter(name_org=pk)
    event_list = Event.objects.filter(name_org=pk)
    return render(request, 'page_org.html', {"org": org_list, "class": class_list, "event": event_list})


def choose_org_view(request):
    org_list = Organization.objects.all()
    return render(request, 'choose_org.html', {"orgs": org_list})
