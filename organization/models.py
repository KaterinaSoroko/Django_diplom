from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Organization(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name_org = models.CharField(max_length=100, verbose_name='Название')
    description_org = models.TextField(verbose_name='Описание')
    address_org = models.CharField(max_length=256, verbose_name='Адрес')
    phone_org = models.CharField(max_length=15, verbose_name='Телефон')
    viber = models.CharField(max_length=15, verbose_name='Viber', null=True, blank=True)
    telegtam = models.CharField(max_length=50, verbose_name='Telegram', null=True, blank=True)
    instagram = models.CharField(max_length=50, verbose_name='Instagram', null=True, blank=True)
    logo = models.ImageField(verbose_name='Логотип', upload_to='logo/', null=True, blank=True)
    created = models.DateField(auto_now=True, verbose_name='Дата регистрации')
    publication = models.BooleanField(default=False, verbose_name="Публикация")

    def __str__(self):
        return self.name_org

    class Meta:
        db_table = "organization"
        unique_together = ("name_org", "address_org")


class OrgEducatuion(models.Model):
    name_org = models.CharField(max_length=100, verbose_name='Название')
    description_org = models.TextField(verbose_name='Описание')
    address_org = models.CharField(max_length=256, verbose_name='Адрес')
    phone_org = models.CharField(max_length=15, verbose_name='Телефон')
    logo = models.ImageField(verbose_name='Логотип', upload_to='logo/', null=True, blank=True)

    def __str__(self):
        return self.name_org

    class Meta:
        db_table = "organization_orgeducatuion"

