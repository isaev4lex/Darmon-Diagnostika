from django.db import models
from .ru_to_eng import translate
from django.urls import reverse


class LoreItem(models.Model):
    title_ru = models.CharField(max_length=300, verbose_name='Название (РУС)', blank=False, unique=True)
    description_ru = models.TextField(verbose_name='Описание (РУС)', blank=False)

    title_uz = models.CharField(max_length=300, verbose_name='Название (УЗБ)', blank=False, unique=True)
    description_uz = models.TextField(verbose_name='Описание (УЗБ)', blank=False)

    slug = models.CharField(max_length=300, verbose_name='URL (Необязательно)', blank=True, unique=True)

    class Meta:
        verbose_name = 'Информацию для страницы ЛОР'
        verbose_name_plural = 'Информация для страницы ЛОР'

    def __str__(self):
        return self.title_ru

    def get_url_ru(self):
        return reverse("lore_slug_ru", args=[self.slug])

    def get_url_uz(self):
        return reverse("lore_slug_uz", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translate(self.title_ru)
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

