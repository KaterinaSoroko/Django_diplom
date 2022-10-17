import re

from django import forms
from django.core.exceptions import ValidationError

from organization.models import Organization


class OrganizationForm(forms.ModelForm):

    class Meta:
        model = Organization
        fields = ('name_org', 'description_org', 'address_org', 'phone_org', 'viber',
                  'telegtam', 'instagram', 'logo', 'publication')
        labels = {
            "name_org": "Название организации",
            "description_org": "Описание организации",
            "address_org": "Адрес организации",
            "phone_org": "Номер телефона"
        }
        help_texts = {
        "phone_org": "Введите телефон в формате '+375299999999'",
        "viber": "Введите телефон в формате '+375299999999' (необязательное)",
        "telegtam": "Введите имя пользователя в формате '@username' или номер телефона в формате '+375299999999' (необязательное)",
        "instagram": "Введите имя пользователя в формате '@username' (необязательное)",
        "publication": "Для отображения в списке организаций"
        }

    def clean_phone_org(self):
        phone = self.cleaned_data["phone_org"]
        if not re.fullmatch(r"^(\+375)+[0-9]{9}$", phone):
            raise ValidationError('Телефон введен не корректно')
        return phone

    def clean_viber(self):
        phone = self.cleaned_data["viber"]
        if not re.fullmatch(r"^(\+375)+[0-9]{9}$", phone):
            raise ValidationError('Телефон введен не корректно')
        return phone

    def clean_telegtam(self):
        slack = self.cleaned_data["telegtam"]
        if not re.fullmatch(r"^(@)[0-9a-zA-Z]+", slack):
            raise ValidationError('Телефон введен не корректно')
        return slack

    def clean_instagram(self):
        slack = self.cleaned_data["instagram"]
        if not re.fullmatch(r"^(@)[0-9a-zA-Z]+", slack):
            raise ValidationError('Телефон введен не корректно')
        return slack
