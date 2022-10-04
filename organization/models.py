from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Organization(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name_org = models.CharField(max_length=100, verbose_name='Название')
    description_org = models.TextField(verbose_name='Описание')
    address_org = models.CharField(max_length=256, verbose_name='Адрес')
    phone_org = models.CharField(max_length=15, verbose_name='Телефон')
    email = models.EmailField(verbose_name='E-mail')
    viber = models.CharField(max_length=15, verbose_name='Viber', null=True, blank=True)
    telegtam = models.CharField(max_length=50, verbose_name='Telegram', null=True, blank=True)
    instagram = models.CharField(max_length=50, verbose_name='Instagram', null=True, blank=True)
    vk = models.CharField(max_length=256, verbose_name='ВКонтакте', null=True, blank=True)
    ok = models.CharField(max_length=256, verbose_name='Одноклассники', null=True, blank=True)
    logo = models.ImageField(verbose_name='Логотип', upload_to='logo/', null=True, blank=True)
    created = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')
    # confirm_data = models.BooleanField()

    def __str__(self):
        return self.name_org

    def get_absolut_url(self):
        return reverse('page_org', kwargs={'org_id': self.pk})

    class Meta:
        db_table = "organization"
        unique_together = ("name_org", "address_org")
