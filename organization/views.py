from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from organization.models import Organization
from organization.forms import OrganizationForm
from classes.models import Classes
from event.models import Event


def create_org_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse('log_in'))
    if request.method == 'POST':
        form = OrganizationForm(request.POST, request.FILES)
        if form.is_valid():
            f_org = form.save(commit=False)
            f_org.username = User.objects.get(username=request.user)
            f_org.save()
            return redirect("page_user", request.user.id)
    else:
        form = OrganizationForm()
    content = {"org_form": form}
    return render(request, 'create_org.html', content)


def page_org_view(request, pk):
    org_list = get_object_or_404(Organization, pk=pk)
    if org_list.username == request.user:
        class_list = Classes.objects.filter(name_org=pk)
        event_list = Event.objects.filter(name_org=pk)
    else:
        if org_list.publication:
            class_list = Classes.objects.filter(Q(name_org=pk) & Q(publication=True))
            event_list = Event.objects.filter(Q(name_org=pk) & Q(publication=True))
        else:
            return render(request, "no_access.html")
    return render(request, 'page_org.html', {"org": org_list, "class": class_list, "event": event_list})


def choose_org_view(request):
    org_list = Organization.objects.filter(publication=True)
    return render(request, 'choose_org.html', {"orgs": org_list})
