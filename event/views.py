import datetime
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from event.models import Event
from event.forms import EventForms
from organization.models import Organization


class PageEventView(DetailView):
    model = Event
    template_name = "page_event.html"


class CreateEventView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse('log_in'))
        form = EventForms()
        content = {"form": form}
        return render(request, 'create_event.html', content)

    def post(self, request):
        form = EventForms(request.POST, request.FILES)
        if form.is_valid():
            f_event = form.save(commit=False)
            user_id = User.objects.get(username=request.user)
            f_event.username = user_id
            p_org = Organization.objects.get(username=request.user)
            f_event.name_org = p_org
            f_event.save()
            return redirect("page_user", user_id.id)


class UpdateEventView(UpdateView):
    model = Event
    fields = ('name_event', 'description_event', 'address_event', 'date_event', 'time_event',
              'age_event', 'price_event', 'price_reference', 'phone_reference', 'poster',
              'publication')
    template_name = 'create_event.html'


class UpdatePubEventView(UpdateView):
    model = Event
    fields = ('publication',)
    template_name = 'publication.html'


class DeleteEventView(DeleteView):
    model = Event
    template_name = 'delete.html'
    success_url = reverse_lazy('about_fanipol')

class ChoiceEventView(ListView):
    paginate_by = 5
    model = Event
    template_name = 'choice_event.html'

    def get_queryset(self):
        return Event.objects.filter(Q(publication=True) & Q(date_event__gt=datetime.date.today())).order_by("date_event")
