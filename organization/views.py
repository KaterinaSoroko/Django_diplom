import datetime
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from organization.models import Organization
from organization.forms import OrganizationForm
from classes.models import Classes
from event.models import Event


class CreateOrgView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse('log_in'))
        form = OrganizationForm()
        content = {"form": form}
        return render(request, 'create_org.html', content)

    def post(self, request):
        form = OrganizationForm(request.POST, request.FILES)
        if form.is_valid():
            f_org = form.save(commit=False)
            f_org.username = User.objects.get(username=request.user)
            f_org.save()
            return redirect("page_user", request.user.id)


def page_org_view(request, pk):
    org_list = get_object_or_404(Organization, pk=pk)
    if org_list.username == request.user:
        class_list = Classes.objects.filter(name_org=pk)
        event_list = Event.objects.filter(Q(name_org=pk) & Q(date_event__gt=datetime.date.today())).order_by("date_event")
    else:
        if org_list.publication:
            class_list = Classes.objects.filter(Q(name_org=pk) & Q(publication=True))
            event_list = Event.objects.filter(Q(name_org=pk) & Q(publication=True)& Q(date_event__gt=datetime.date.today())).order_by("date_event")
        else:
            return render(request, "no_access.html")
    return render(request, 'page_org.html', {"org": org_list, "class": class_list, "event": event_list})


class ChoiceOrgView(ListView):
    paginate_by = 10
    model = Organization
    template_name = "choice_org.html"

    def get_queryset(self):
        return Organization.objects.filter(publication=True)


class UpdateOrgView(UpdateView):
    model = Organization
    fields = ('name_org', "description_org", "address_org", 'phone_org', "viber", 'telegtam',
              'instagram', 'logo', 'publication')
    template_name = 'create_org.html'

    def get_success_url(self):
        return reverse("page_user", kwargs={"user_id": self.request.user.id})


class UpdatePubOrgView(UpdateView):
    model = Organization
    fields = ('publication',)
    template_name = 'publication.html'
    extra_context = {"title": "Публикация", "text": "Вы уверены, что хотите изменить статус?"}

    def get_success_url(self):
        return reverse("page_user", kwargs={"user_id": self.request.user.id})


class DeleteOrgView(DeleteView):
    model = Organization
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse("page_user", kwargs={"user_id": self.request.user.id})

