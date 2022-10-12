import datetime

from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from event.models import Event
from event.forms import EventForms
from organization.models import Organization


def page_event_view(request, event_id):
    event_list = get_object_or_404(Event, pk=event_id)
    return render(request, 'page_event.html', {"event": event_list})


def create_event_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse('log_in'))
    if request.method == 'POST':
        form = EventForms(request.POST, request.FILES)
        if form.is_valid():
            f_event = form.save(commit=False)
            f_event.username = User.objects.get(username=request.user)
            p_org = Organization.objects.get(username=request.user)
            f_event.name_org = p_org
            f_event.save()
            return redirect("page_org", p_org.id)
    else:
        form = EventForms()
    content = {"event_form": form}
    return render(request, 'create_event.html', content)


def choose_event_view(request):
    events_list = Event.objects.filter(Q(publication=True) & Q(date_event__gt=datetime.date.today())).order_by("date_event")
    return render(request, 'choose_event.html', {"event_list": events_list})
