from django import forms


class ClassForm(forms.Form):
    name_class = forms.CharField()
    name_category = forms.ChoiceField()
    description_class = forms.Textarea()
    address_class = forms.CharField()
    datatime_class = forms.CharField()
    age_class = forms.CharField()
    price_class = forms.CharField()
    phone_reference = forms.CharField()
    poster = forms.ImageField()
