from django import forms


class OrganizationForm(forms.Form):
    name_org = forms.CharField(
        label="Название организации",
        widget=forms.TextInput(attrs={'size': '40', 'class': 'form-input'}),
    )
    description_org = forms.CharField(
        label="Описание организации",
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}),
    )
    address_org = forms.CharField(
        label="Адрес",
        widget=forms.TextInput(attrs={'size': '40'}),
    )
    phone_org = forms.CharField(
        label="Номер телефона",
        help_text="Введите телефон в формате '+375299999999'",
        widget=forms.TextInput(attrs={'size': '40'}),
    )
    viber = forms.CharField(
        label="Viber",
        required=False,
        help_text="Введите телефон в формате '+375299999999' (необязательное)",
        widget=forms.TextInput(attrs={'size': '40'}),
    )
    telegtam = forms.CharField(
        label="Telegram",
        help_text="Введите имя пользователя в формате '@username' (необязательное)",
        required=False,
        widget=forms.TextInput(attrs={'size': '40'}),
    )
    instagram = forms.CharField(
        label="Instagram",
        help_text="Введите имя пользователя в формате '@username' (необязательное)",
        required=False,
        widget=forms.TextInput(attrs={'size': '40'}),
    )
    logo = forms.ImageField(
        label="Логотип",
        required=False,
    )
