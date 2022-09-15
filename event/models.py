from django.db import models
from django.contrib.auth.models import User
from organization.models import Organization


class Event(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    name_org = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name='Название организации')
    name_event = models.CharField(max_length=250, verbose_name='Название')
    description_event = models.TextField(verbose_name='Описание')
    address_event = models.CharField(max_length=256, verbose_name='Адрес')
    date_event = models.DateField(verbose_name="Дата проведения")
    time_event = models.TimeField(verbose_name="Время проведения")
    age_event = models.CharField(max_length=250, null=True, blank=True, verbose_name="Для кого")
    price_event = models.CharField(max_length=250, null=True, blank=True, verbose_name="Цена")
    price_reference = models.TextField(null=True, blank=True, verbose_name='как купить')
    phone_reference = models.CharField(max_length=15, null=True, blank=True, verbose_name='Телефон')
    poster = models.ImageField(verbose_name='Логотип', upload_to='logo/', null=True, blank=True)
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name_event

    class Meta:
        db_table = "event"
