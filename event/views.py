from django.shortcuts import render


def page_event_view(request):
    return render(request, 'page_event.html', {})


def create_event_view(request):
    return render(request, 'create_event.html', {})


def choose_event_view(request):
    return render(request, 'choose_event.html', {})
