import re
import pathlib
from random import randrange
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse, reverse_lazy

from Fanipol import settings


class Organization(models.Model):

    def file_path(self, filename):
        file = pathlib.Path(filename)
        ext = file.suffix or ".pmg"
        random_suffix = str(randrange(1000, 9999))
        path = datetime.strftime(datetime.now(), "logo/orl_logo/logo-%Y%m%d%H%M%S")+random_suffix
        return path + ext


    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name_org = models.CharField(max_length=100, verbose_name='Название')
    description_org = models.TextField(verbose_name='Описание')
    address_org = models.CharField(max_length=256, verbose_name='Адрес')
    phone_org = models.CharField(max_length=15, verbose_name='Телефон')
    viber = models.CharField(max_length=100, verbose_name='Viber', null=True, blank=True)
    telegtam = models.CharField(max_length=100, verbose_name='Telegram', null=True, blank=True)
    instagram = models.CharField(max_length=100, verbose_name='Instagram', null=True, blank=True)
    logo = models.ImageField(verbose_name='Логотип', upload_to=file_path, null=True, blank=True)
    created = models.DateField(auto_now=True, verbose_name='Дата регистрации')
    publication = models.BooleanField(default=False, verbose_name="Публикация")

    def __str__(self):
        return self.name_org
# ToDo сохраненине ссылки на соцсети и картинку

    def get_absolute_url(self):
        return reverse_lazy('page_user', kwargs={"user_id": self.username.id})


    class Meta:
        db_table = "organization"
        unique_together = ("name_org", "address_org")


@receiver(models.signals.pre_save, sender=Organization)
def social_network_save(sender, instance, **kwargs):
    if instance.viber:
        if str(instance.viber).startswith("+375"):
            instance.viber = "viber://chat?number=%2B" + str(instance.viber).strip("+")
        elif not str(instance.viber).startswith("viber"):
            instance.viber = ""
    if instance.telegtam:
        if str(instance.telegtam).startswith("@"):
            instance.telegtam = "https://t.me/" + str(instance.telegtam).strip("@")
        elif not str(instance.telegtam).startswith("https://t.me/"):
            instance.telegtam = ""
    if instance.instagram:
        if str(instance.instagram).startswith("@"):
            instance.instagram = "https://www.instagram.com/" + str(instance.instagram).strip("@")
        elif not str(instance.instagram).startswith("https://www.instagram.com/"):
            instance.instagram = ""


class OrgEducatuion(models.Model):

    def file_path(self, filename):
        file = pathlib.Path(filename)
        ext = file.suffix or ".pmg"
        path = datetime.strftime(datetime.now(), "logo/gos_orl_logo/logo-%Y%m%d%H%M%S")
        return path + ext

    name_org = models.CharField(max_length=100, verbose_name='Название')
    description_org = models.TextField(verbose_name='Описание')
    address_org = models.CharField(max_length=256, verbose_name='Адрес')
    phone_org = models.CharField(max_length=15, verbose_name='Телефон')
    email = models.EmailField(null=True, blank=True, verbose_name='Электронная почта')
    site = models.CharField(max_length=100, null=True, blank=True, verbose_name='Адрес сайта')
    logo = models.ImageField(verbose_name='Логотип', upload_to=file_path, null=True, blank=True)

    def __str__(self):
        return self.name_org

    class Meta:
        db_table = "org_educatuion"

