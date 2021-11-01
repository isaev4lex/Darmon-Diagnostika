from django.db import models
from .ru_to_eng import translate
from django.urls import reverse


class Doctors(models.Model):
    name_ru = models.CharField(max_length=300, verbose_name='Имя (РУС)', blank=False)
    specialty_ru = models.CharField(max_length=200, verbose_name='Специальность (РУС)', blank=False)
    work_days_ru = models.CharField(max_length=300, verbose_name='Дни приёма (РУС)', blank=False)
    description_ru = models.TextField(verbose_name='Образование и опыт работы (РУС)', blank=False)

    name_uz = models.CharField(max_length=300, verbose_name='Имя (УЗБ)', blank=False)
    specialty_uz = models.CharField(max_length=200, verbose_name='Специальность (УЗБ)', blank=False)
    work_days_uz = models.CharField(max_length=300, verbose_name='Дни приёма (УЗБ)', blank=False)
    description_uz = models.TextField(verbose_name='Образование и опыт работы (УЗБ)', blank=False)

    work_from = models.CharField(max_length=300, verbose_name='Начало приёма', blank=False)
    work_to = models.CharField(max_length=300, verbose_name='Конец смены', blank=False)
    photo = models.ImageField(upload_to='media', verbose_name='Фотография', blank=False)
    slug = models.CharField(max_length=300, verbose_name='URL (Необязательно)', blank=True, unique=True)

    class Meta:
        verbose_name = 'Врача'
        verbose_name_plural = 'Врачи'

    def __str__(self):
        return self.name_ru

    def get_url_ru(self):
        return reverse("doctor_slug_ru", args=[self.slug])

    def get_url_uz(self):
        return reverse("doctor_slug_uz", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translate(self.name_ru)
        super().save(*args, **kwargs)


class MetaTags(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title', blank=False)
    keywords = models.TextField(verbose_name='Keywords (Через запятую/Предложением)', blank=False)
    description = models.TextField(verbose_name='Description', blank=False)

    class Meta:
        verbose_name = 'Мета тег'
        verbose_name_plural = 'Мета теги'

    def __str__(self):
        return self.title

