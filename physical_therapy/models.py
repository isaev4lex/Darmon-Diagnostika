from django.db import models
from .ru_to_eng import translate
from django.urls import reverse


class PhysicalTherapy(models.Model):
    banner = models.ImageField(upload_to='media', verbose_name='Картинка')
    description_ru = models.TextField(verbose_name='Содержание (РУС)', blank=False)
    description_uz = models.TextField(verbose_name='Содержание (УЗБ)', blank=False)

    class Meta:
        verbose_name = 'Текст для страницы физиотерапия'
        verbose_name_plural = 'Текста для страницы физиотерапия'

    def __str__(self):
        return 'Описание'


class MetaTags(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title', blank=False)
    keywords = models.TextField(verbose_name='Keywords (Через запятую/Предложением)', blank=False)
    description = models.TextField(verbose_name='Description', blank=False)

    class Meta:
        verbose_name = 'Мета тег'
        verbose_name_plural = 'Мета теги'

    def __str__(self):
        return self.title

