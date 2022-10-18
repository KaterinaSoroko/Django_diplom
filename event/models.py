import pathlib
from datetime import datetime
from random import randrange
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from organization.models import Organization


class Event(models.Model):

    @staticmethod
    def file_path(filename):
        file = pathlib.Path(filename)
        ext = file.suffix or ".pmg"
        random_suffix = str(randrange(1000, 9999))
        path = datetime.strftime(datetime.now(), "logo/event_poster/%Y/poster-%m%d%H%M%S")+random_suffix
        return path + ext

    username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    name_org = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name='Название организации')
    name_event = models.CharField(max_length=250, verbose_name='Название')
    description_event = models.TextField(verbose_name='Описание')
    address_event = models.CharField(max_length=256, verbose_name='Адрес')
    date_event = models.DateField(verbose_name="Дата проведения")
    time_event = models.TimeField(verbose_name="Время проведения")
    age_event = models.CharField(max_length=250, null=True, blank=True, verbose_name="Для кого")
    price_event = models.CharField(max_length=250, null=True, blank=True, verbose_name="Цена")
    price_reference = models.CharField(max_length=256, null=True, blank=True, verbose_name='как купить')
    phone_reference = models.CharField(max_length=15, null=True, blank=True, verbose_name='Телефон')
    poster = models.ImageField(verbose_name='Афиша', upload_to=file_path, null=True, blank=True)
    created = models.DateField(auto_now=True, verbose_name='Дата создания')
    publication = models.BooleanField(default=False, verbose_name='Публикация')

    def __str__(self):
        return self.name_event

    def get_absolute_url(self):
        return reverse_lazy('page_user', kwargs={"user_id": self.username.id})

    class Meta:
        db_table = "event"
