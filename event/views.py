from django.shortcuts import render, get_object_or_404
from event.models import Event
from event.forms import EventForms


def page_event_view(request, event_id):
    event_list = get_object_or_404(Event, pk=event_id)
    return render(request, 'page_event.html', {"event": event_list})


def create_event_view(request):
    if request.method == 'POST':
        form = EventForms(request.POST)
    else:
        form = EventForms()
    content = {"event_form": form}
    return render(request, 'create_event.html', content)


def choose_event_view(request):
    events_list = Event.objects.all()
    return render(request, 'choose_event.html', {"event_list": events_list})
