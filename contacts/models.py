from django.db import models


class PhoneNumbers(models.Model):
    number = models.CharField(max_length=18, verbose_name='Номер')
    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'

    def __str__(self):
        return self.number


class Emails(models.Model):
    email = models.CharField(max_length=100, verbose_name='Почта')

    class Meta:
        verbose_name = 'Email адрес'
        verbose_name_plural = 'Email адреса'

    def __str__(self):
        return self.email


class Addresses(models.Model):
    address = models.TextField(verbose_name='Адрес (Рус)')
    address_uz = models.TextField(verbose_name='Адрес (Узб)')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.address


class MetaTags(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title', blank=False)
    keywords = models.TextField(verbose_name='Keywords (Через запятую/Предложением)', blank=False)
    description = models.TextField(verbose_name='Description', blank=False)

    class Meta:
        verbose_name = 'Мета тег'
        verbose_name_plural = 'Мета теги'

    def __str__(self):
        return self.title

