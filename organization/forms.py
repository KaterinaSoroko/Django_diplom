from django import forms
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

