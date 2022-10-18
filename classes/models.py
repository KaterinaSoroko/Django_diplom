import pathlib
from datetime import datetime
from random import randrange
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from organization.models import Organization


class Category(models.Model):
    name_category = models.CharField(max_length=250)

    def __str__(self):
        return self.name_category

    class Meta:
        db_table = "category"


class Classes(models.Model):

    @staticmethod
    def file_path(filename):
        file = pathlib.Path(filename)
        ext = file.suffix or ".pmg"
        random_suffix = str(randrange(1000, 9999))
        path = datetime.strftime(datetime.now(), "logo/class_logo/poster-%Y%m%d%H%M%S")+random_suffix
        return path + ext

    username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    name_org = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        verbose_name='Название организации',
    )
    name_class = models.CharField(max_length=150, verbose_name='Название')
    name_category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, verbose_name='Категория')
    description_class = models.TextField(verbose_name='Описание')
    address_class = models.CharField(max_length=256, null=True, blank=True, verbose_name='Адрес')
    datatime_class = models.CharField(max_length=256, null=True, blank=True,  verbose_name="Время проведения")
    age_class = models.CharField(max_length=100, null=True, blank=True, verbose_name="Для кого")
    price_class = models.CharField(max_length=50, null=True, blank=True, verbose_name="Цена")
    phone_reference = models.CharField(max_length=15, null=True, blank=True, verbose_name='Телефон')
    poster = models.ImageField(verbose_name='Имя файла', upload_to=file_path, null=True, blank=True)
    created = models.DateField(auto_now=True, verbose_name='Дата создания')
    publication = models.BooleanField(default=False, verbose_name='Публикация')

    def __str__(self):
        return self.name_class

    def get_absolute_url(self):
        return reverse_lazy('page_user', kwargs={"user_id": self.username.id})

    class Meta:
        db_table = "classes"


class Age_list(models.Model):
    age_option = models.CharField(max_length=250)

    class Meta:
        db_table = "age_list"

    def __str__(self):
        return self.age_option


class Age(models.Model):
    name_class = models.ForeignKey(Classes, on_delete=models.CASCADE, verbose_name="Название занятия")
    age = models.ForeignKey(Age_list, on_delete=models.CASCADE, verbose_name="Название занятия")

    class Meta:
        db_table = "age"

    def __str__(self):
        return self.pk


class Photo(models.Model):

    @staticmethod
    def file_path(filename):
        file = pathlib.Path(filename)
        ext = file.suffix or ".pmg"
        random_suffix = str(randrange(1, 999999))
        path = datetime.strftime(datetime.now(), "photo/class/photo-%Y%m%d%H%M%S")+random_suffix
        return path + ext

    name_class = models.ForeignKey(Classes, on_delete=models.CASCADE,  verbose_name="Название занятия")
    name_photo = models.ImageField(verbose_name='Имя файла', upload_to=file_path)

    class Meta:
        db_table = "photo"
