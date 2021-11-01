from django.db import models


class PriceCategory(models.Model):
    title_ru = models.CharField(max_length=300, verbose_name='Название (РУС)')
    title_uz = models.CharField(max_length=300, verbose_name='Название (УЗБ)')

    class Meta:
        verbose_name = 'Категорию в Price List'
        verbose_name_plural = 'Категории в Price List'

    def __str__(self):
        return self.title_ru


class PriceSubCategory(models.Model):
    category = models.ForeignKey(PriceCategory, on_delete=models.CASCADE, verbose_name='Для категории')
    title_ru = models.CharField(max_length=300, verbose_name='Услуга (РУС)')
    title_uz = models.CharField(max_length=300, verbose_name='Услуга (УЗБ)')
    price = models.CharField(max_length=11, verbose_name='Цена')

    class Meta:
        verbose_name = 'Услугу в Price List'
        verbose_name_plural = 'Услуги в Price List'


class MetaTags(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title', blank=False)
    keywords = models.TextField(verbose_name='Keywords (Через запятую/Предложением)', blank=False)
    description = models.TextField(verbose_name='Description', blank=False)

    class Meta:
        verbose_name = 'Мета тег'
        verbose_name_plural = 'Мета теги'

    def __str__(self):
        return self.title

