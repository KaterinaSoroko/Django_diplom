from django import forms


class EventForms(forms.Form):
    name_event = forms.CharField()
    description_event = forms.Textarea()
    address_event = forms.CharField()
    date_event = forms.DateField()
    time_event = forms.TimeField()
    age_event = forms.CharField()
    price_event = forms.CharField()
    price_reference = forms.Textarea()
    phone_reference = forms.CharField()
    poster = forms.ImageField()
