import datetime
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from event.models import Event
from event.forms import EventForms
from organization.models import Organization


class PageEventView(DetailView):
    model = Event
    template_name = "page_event.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['org_list'] = get_object_or_404(Organization, username=self.object.username_id)
        return context


class CreateEventView(View):

    @staticmethod
    def get(request):
        if not request.user.is_authenticated:
            return redirect(reverse('log_in'))
        form = EventForms()
        content = {"form": form,
                   "title": "Добавление мероприятия",
                   "button": "Добавить мероприятие",
                   }
        return render(request, 'update_in_form.html', content)

    @staticmethod
    def post(request):
        form = EventForms(request.POST, request.FILES)
        if form.is_valid():
            f_event = form.save(commit=False)
            user_id = User.objects.get(username=request.user)
            f_event.username = user_id
            p_org = Organization.objects.get(username=request.user)
            f_event.name_org = p_org
            f_event.save()
            return redirect("page_user", user_id.id)
        content = {"form": form,
                   "title": "Добавление мероприятия",
                   "button": "Добавить мероприятие",
                   }
        return render(request, 'update_in_form.html', content)


class UpdateEventView(UpdateView):
    model = Event
    form_class = EventForms
    template_name = 'update_in_form.html'
    extra_context = {
        "title": "Изменение мероприятия",
        "text": "Внесите изменения:",
        "button": "Сохранить изменения",
    }

    def get_success_url(self):
        return reverse("page_user", kwargs={"user_id": self.request.user.id})


class UpdatePubEventView(UpdateView):
    model = Event
    fields = ('publication',)
    template_name = 'update_delete.html'
    extra_context = {
        "title": "Публикация",
        "text": "Вы уверены, что хотите изменить статус?",
        "button": "Изменить статус"
    }

    def get_success_url(self):
        return reverse("page_user", kwargs={"user_id": self.request.user.id})


class DeleteEventView(DeleteView):
    model = Event
    template_name = 'update_delete.html'
    extra_context = {
        "title": "Удаление мероприятия",
        "text": "Вы уверены, что хотите удалить мероприятие?",
        "button": "Удалить мероприятие",
    }

    def get_success_url(self):
        return reverse("page_user", kwargs={"user_id": self.request.user.id})


class ChoiceEventView(ListView):
    paginate_by = 5
    model = Event
    template_name = 'choice_event.html'

    def get_queryset(self):
        return Event.objects.filter(Q(publication=True) & (Q(date_event__gt=datetime.date.today()) | Q(date_event=datetime.date.today()))).order_by("date_event")

    def get_success_url(self):
        return reverse("page_user", kwargs={"user_id": self.request.user.id})
