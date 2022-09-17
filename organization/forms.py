from django import forms


class OrganizationForm(forms.Form):
    name_org = forms.CharField()
    description_org = forms.CharField(wiaget=forms.Textarea())
    address_org = forms.CharField()
    phone_org = forms.CharField()
    email = forms.EmailField()
    viber = forms.CharField()
    telegtam = forms.CharField()
    instagram = forms.CharField()
    vk = forms.CharField()
    ok = forms.CharField()
    logo = forms.ImageField()
