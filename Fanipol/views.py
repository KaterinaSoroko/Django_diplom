from django.shortcuts import render
from Fanipol.content import text_about_fanipol, text_pegistration_rules
from organization.models import OrgEducatuion


def fanipol_view(request):
    org_list = OrgEducatuion.objects.all()
    return render(request, 'about_fanipol.html', {"orgs": org_list, "text_page": text_about_fanipol})


def registration_view(request):
    return render(request, 'registration_rules.html', {"text_page": text_pegistration_rules})

def no_access_view(request):
    return render(request, 'no_access.html')
